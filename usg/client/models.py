from django.db import models
from django.contrib.auth.models import AbstractUser
from firebase_admin import auth

class CustomUser(AbstractUser):
    UID = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    tel = models.CharField(max_length=16, null=True)
    user_profile_img = models.ImageField(upload_to='images/', null=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Untuk membuat pengguna baru di Firebase saat menyimpan
            firebase_user = auth.create_user(
                email=self.email,
                email_verified=False,  
                password=self.password, 
                display_name=self.name,
                phone_number=self.tel if self.tel else None
                # Tambahkan bidang lain jika perlu
            )
            self.UID = firebase_user.uid  # Simpan UID Firebase ke dalam model Django
        else:  # Untuk memperbarui pengguna Firebase saat instance disimpan ulang
            firebase_user = auth.get_user(self.UID)
            firebase_user.update_display_name(self.name)
            firebase_user.update_email(self.email)
            # Lakukan pembaruan bidang lain jika perlu

        super().save(*args, **kwargs)  # Simpan model Django

    def delete(self, *args, **kwargs):
        firebase_user = auth.get_user(self.UID)
        auth.delete_user(firebase_user.uid)  # Hapus pengguna Firebase saat instance dihapus
        super().delete(*args, **kwargs)  # Hapus model Django
