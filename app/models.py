from django.db import models

# Create your models here.
class Department(models.Model):
    # 部门表
    title = models.CharField(verbose_name="部门名字", max_length=32)
    
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    # 员工表
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    # 余额最大长度是0，两位小数，初始值默认是0
    account = models.DecimalField(verbose_name="余额",max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    #无约束
    # depart_id = models.BigIntegerField(verbose_name="部门id")
    # 有约束
    # to 与哪张表关联
    # to_field 与表中的哪一列关联
    # 第一种方法：models.CASCADE 表示级联删除，如果部门表某个部门删除，对应的id下所有的员工也会删除
    depart_id = models.ForeignKey(verbose_name="部门",to="Department", to_field="id", on_delete=models.CASCADE)

    # 第二种方法：置空
    # depart_id = models.ForeignKey(to="Department", to_field="id",null=True, blank=True, on_delete=models.SET_NULL)

    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    
    
class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)
    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    status_choices = (
        (1, "已占用"),
        (2, "未占用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)
