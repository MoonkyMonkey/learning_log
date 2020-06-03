# learning_log
Learn Python book demo

### 创建网页过程

1. 定义 url
2. 编写试图
3. 编写模板

个人觉得好的顺序 321 这样可以先不能访问到在编写的模板 需要访问时再加入 url

### 修改 models 的三个步骤
1. 修改 models.py
2. 对 app 调用 makemigrations
3. 调用 migrate

- flush 重建数据库（会丢失所有数据）
### 创建 app

1. python manage.py startapp xxx
2. 在 settings 中加入 app
3. urls 加入新的路径

### 美化引入 bootstrap3

- settings 中添加

### 限制用户登录才能访问

- 添加 login_required 装饰器并添加在需要的 view 函数中
- 修改设置使其可以跳转到 login 界面
- 使数据关联到用户， 给表添加 owner 属性
- 迁移数据
- 给展示页面添加 filter 过滤出当前用户的数据
- 限制不同用户无法互相访问到
- 修改 view 使表单能关联到对应的用户

### 部署

heroku config:set DISABLE_COLLECTSTATIC=1

#### problem 

- path 和 url 的区别，哪个版本更改的
- urls namespace 参数无法加入
- django reverse 函数位置修改
- 内嵌类 Meta 的作用
- entry 页面显示问题
- 防止快速多重点击添加多个topic
