## 用法

本文件用于将每月的账单从notion保存到beancount.

[Beancount —— 命令行复式簿记](https://wzyboy.im/post/1063.html)

[Notion 月账单模板](https://wary-pendulum-590.notion.site/8b0e1616c5024cd6bfadf288df27648c?pvs=4)

[记账神器 Beancount 教程](https://sspai.com/post/59777)

## 我的beancount文件
和网上分享的多层文件一致,每月账单的路径为`YYYY/M.bean`, `Expenses:XXX`存储于`accounts/expenses.bean`,对应了生成月账单的支出类型.

```
#expense.bean
option "title" "expenses"
option "operating_currency" "CNY"


; 2001-08-06 open Expenses:Unknown CNY
2001-08-06 open Expenses:Other  CNY
2001-08-06 open Expenses:Dining  CNY
2001-08-06 open Expenses:Shopping  CNY
2001-08-06 open Expenses:Transportation  CNY
2001-08-06 open Expenses:Entertainment  CNY
2001-08-06 open Expenses:Electronics  CNY
2001-08-06 open Expenses:Clothing  CNY
2001-08-06 open Expenses:Pets  CNY
2001-08-06 open Expenses:Daily  CNY
2001-08-06 open Expenses:SnacksandBeverages  CNY
2001-08-06 open Expenses:FruitsandVegetables  CNY
```

## 使用方式
每月记账完成后进入月账单的`database`,点击右上角`...=>Export`,选项`Markdown&CSV/Everything/Everyting`,解压导出的zip,将其放在和`import.py`同路径下运行以下命令.
```
python import.py
```
> PS:因为我的记录方法为每月统计一次,因此生成的bean文件以database内第一笔账的月份为名.
