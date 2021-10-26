from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models import Max
from uuid import uuid4
from mptt.models import  MPTTModel, TreeForeignKey
from django.utils import timezone
# Create your models here.

accountType = [
    ("MEMBER", "MEMBER"),
    ("ADMIN", "ADMIN"),
]


bankType = [
    ("-","-"),
    ("MAYBANK", "MAYBANK"),
    ("PUBLIC BANK", "PUBLIC BANK"),
    ("RHB", "RHB"),
    ("HSBC", "HSBC"),
    ("CIMB", "CIMB"),
    ("HONG LEONG", "HONG LEONG"),
    ("AMBANK", "AMBANK"),
    ("ALLIANCE BANK", "ALLIANCE BANK"),
]

def generateUUID():
    return str(uuid4().hex)



class MyAccountManager(BaseUserManager):
    def create_user(self, username, password):
        # if not email:
        #     raise ValueError("Email Required")
        if not username:
            raise ValueError("Username Required")
        # if not user_pin:
        #     raise ValueError("PIN Required")
        # if not full_name:
        #     raise ValueError("Full Name Required")
        # if not ic_number:
        #     raise ValueError("IC Number Required")
        # if not user_mobile:
        #     raise ValueError("Mobile Required")

        user = self.model(
            username = username,
            #email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):
        user = self.create_user(
            #email = self.normalize_email(email),
            username = username,
            password = password,
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)





class Account(AbstractBaseUser, MPTTModel, PermissionsMixin):
    #Default Required
    username = models.CharField(max_length=30, unique=True)
    raw_password = models.CharField(max_length=30, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', default=timezone.now)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    #Added
    # testestst

    #system essential
    id = models.AutoField(primary_key=True, editable=False)
    referral = models.CharField(max_length=40, unique=True, default=generateUUID)

    #Personal Deetails
    avatar = models.ImageField(upload_to='avatar_image', blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    ic_number = models.IntegerField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    user_pin = models.IntegerField(null=True, blank=True)
    user_mobile = models.CharField(max_length=20, null=True, blank=True)

    #Bank Details
    bank_country = models.CharField(max_length=20, null=True, blank=True)
    bank_name = models.CharField(max_length=50, choices=bankType, null=True, blank=True)
    bank_holder_name = models.CharField(max_length=100, null=True, blank=True)
    bank_number = models.CharField(max_length=50, null=True, blank=True)
    user_usdt_wallet = models.CharField(max_length=100, null=True, blank=True)

    #Wallet
    diamond = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    ruby = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    gold = models.DecimalField(default=0, max_digits=10, decimal_places=3)


    #Rank System
    account_type = models.CharField(max_length=20, choices=accountType, default='MEMBER')

    class MPTTMeta:
        # level_attr =    'mppt_level'
        order_insertion_by = ['username']


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True