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

### 部署
heroku config:set DISABLE_COLLECTSTATIC=1
#### problem 

- path 和 url 的区别，哪个版本更改的
- urls namespace 参数无法加入
- django reverse 函数位置修改
- 内嵌类 Meta 的作用
- entry 页面显示问题
