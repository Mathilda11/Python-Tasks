# Python-Tasks
## 🍉页面级爬虫
-  :cherry_blossom:[爬取136book网站上的小说](https://github.com/Mathilda11/Python-Tasks/tree/master/crawl_novel)

基于Requests库和BeautifulSoup库。

- 步骤
   - 调用Requests库获得一个请求回应
   - 调用BeautifulSoup库的lxml解析器来解析页面内容
   - 对解析的soup进行查找匹配：
      使用选择器查找标签内容，调用re库使用正则表达式对某些内容进行过滤
    - 对爬取的内容进行格式处理并保存到本地

## 🍒与微信交互
-  :palm_tree:[实现adidas公众号自动回复抢购](https://github.com/Mathilda11/Python-Tasks/tree/master/wechat)  

- 任务：
   - 从公众号回复中获取发送个人信息格式，发送正确的个人信息。
   - 根据公众号发送的计算题（可能包含中文），计算回复答案。

基于itchat微信接口、APScheduler定时任务框架。
- 步骤
   - 登录微信（二维码）
   - 获取自己的用户信息，返回自己的属性字典
   - 编写自动给公众号发送消息的任务，利用APScheduler定时发送

