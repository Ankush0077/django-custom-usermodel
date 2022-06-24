from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            '+919999999999', '666666')
        self.assertEqual(super_user.phone_number, '+919999999999')
        self.assertEqual(super_user.current_otp, '666666')
        self.assertFalse(super_user.is_phone_verified)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "+919999999999")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                phone_number='+919999999999', current_otp='666666', is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                phone_number='+919999999999', current_otp='666666', is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                phone_number='', current_otp='666666', is_superuser=True)
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                phone_number='+919999999999', current_otp='', is_superuser=True)
            
    # def test_new_staffuser(self):
    #     db = get_user_model()
    #     staff_user = db.objects.create_staffuser(
    #         '+919999999999', '666666')
    #     self.assertEqual(staff_user.phone_number, '+919999999999')
    #     self.assertEqual(staff_user.current_otp, '666666')
    #     self.assertFalse(staff_user.is_phone_verified)
    #     self.assertFalse(staff_user.is_superuser)
    #     self.assertTrue(staff_user.is_staff)
    #     self.assertTrue(staff_user.is_active)
    #     self.assertEqual(str(staff_user), "+919999999999")

    #     with self.assertRaises(ValueError):
    #         db.objects.create_staffuser(
    #             phone_number='+919999999999', current_otp='666666', is_superuser=True)

    #     with self.assertRaises(ValueError):
    #         db.objects.create_staffuser(
    #             phone_number='+919999999999', current_otp='666666', is_staff=False)

    #     with self.assertRaises(ValueError):
    #         db.objects.create_staffuser(
    #             phone_number='', current_otp='666666', is_staff=True)
            
    #     with self.assertRaises(ValueError):
    #         db.objects.create_staffuser(
    #             phone_number='+919999999999', current_otp='', is_staff=True)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            '+919999999999', '666666')
        self.assertEqual(user.phone_number, '+919999999999')
        self.assertEqual(user.current_otp, '666666')
        self.assertFalse(user.is_phone_verified)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertEqual(str(user), "+919999999999")
        
        with self.assertRaises(ValueError):
            db.objects.create_user(
                phone_number='', current_otp='666666')
        
        with self.assertRaises(ValueError):
            db.objects.create_user(
                phone_number='+919999999999', current_otp='')