from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator, \
    NumericPasswordValidator

User = get_user_model()


class UserMinimumLengthValidator(MinimumLengthValidator):
    """修改密码最小长度为4位"""

    def __init__(self, min_length=4):
        super(UserMinimumLengthValidator, self).__init__(min_length)
        self.min_length = min_length


class UserCommonPasswordValidator(CommonPasswordValidator):
    """修改密码不做常见性检测"""

    def validate(self, password, user=None):
        pass


class UserNumericPasswordValidator(NumericPasswordValidator):
    """不限制密码全部为数字"""

    def validate(self, password, user=None):
        pass
