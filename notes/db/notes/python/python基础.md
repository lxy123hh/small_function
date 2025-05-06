[TOC]

# 01.Python环境部署.md

# Python介绍

> Life is short, I need python（人生苦短，我用python！）

## Python起源

Python的作者是著名的"**龟叔**"Guido van Rossum(吉多.范罗苏姆)，1989年，龟叔为了打发无聊的圣诞节，决心开发一个新的**解释程序**，作为ABC语言的一种继承。于是便开始编写Python语言。

<img src="/static/notes_picture/python/python基础/image-20240902103540169.png" alt="image-20240902103540169" style="zoom: 80%;" />

**ABC**是由吉多参加设计的一种教学语言，就吉多本人看来，ABC这种语言非常优美和强大，是**专门为非专业程序员设计的**。但是ABC语言并没有成功。**Guido**本人看来，**ABC**失败的原因是高级语言为时过早，并且平台迁移能力弱，难以添加新功能，仅仅专注于编程初学者，没有把有经验的编程人员纳入其中，在**Python**中解决了这些问题，让拓展模块的编写非常容易，并且可以在多平台进行运行....

Python的意思是蟒蛇，是取自英国20世纪70年代首播的电视喜剧《蒙提.派森干的飞行马戏团》(Monty Python’s Flying Circus)，Guido非常喜欢这个剧，所以选择Python作为新语言的名字。

**1991年**，第一个Python编译器诞生。它是用C语言实现的，并能够调用C语言的库文件。

## 解释型和编译型语言

解释型语言是指在运行时由解释器逐行读取和执行源代码的语言。在这种语言中，代码不需要被提前编译成机器代码，而是直接由解释器逐行解析并执行。这使得开发过程更加灵活，程序员可以快速测试和修改代码。Python、JavaScript 和 Ruby 等都是常见的解释型语言。尽管解释型语言在开发时提供了便利，但由于逐行解释执行，通常在性能上不如编译型语言。

编译型语言则是指在执行之前，源代码需要通过编译器转换成机器代码或中间代码。这个过程通常会产生一个独立的可执行文件，运行时不再需要源代码或编译器。这种做法通常能提高程序的执行效率，因为编译后的代码可以直接在机器上运行。C、C++ 和 Go 等语言都是编译型语言。虽然编译型语言在执行速度上表现出色，但编译过程通常较长，调试和修改代码时也不如解释型语言方便

## 编程语言排行

- [TIOBE Index](https://www.tiobe.com/tiobe-index/)
- [PYPL Index](https://pypl.github.io/PYPL.html)

<img src="/static/notes_picture/python/python基础/image-20240920215125704.png" alt="image-20240920215125704" style="zoom:80%;" />

## Python应用领域

**人工智能** 

Python 是人工智能和机器学习领域的首选语言，主要得益于其简洁的语法和丰富的科学计算库。以下是几种典型的 Python 库：

- **NumPy**：支持大量的维度数组与矩阵运算，此外也针对数组运算提供了大量的数学函数库。
- **SciPy**：基于 NumPy 的科学计算库，提供了许多算法和函数，适用于数值积分与优化、线性代数、统计等科学计算任务。
- **Matplotlib**：强大的绘图库，可以生成各种图形，包括线图、散点图、柱状图等，常用于数据可视化。
- **TensorFlow**：由 Google 开发的开源深度学习框架，广泛用于构建和训练神经网络。

**云计算** 

Python 是云计算领域最火的语言之一，广泛用于构建和管理云基础设施。Python 的简洁性和可读性使得它成为开发云服务、自动化任务、数据处理脚本的理想选择。

**WEB开发** 

Python 拥有众多优秀的 Web 框架，适合快速开发高效、安全的 Web 应用程序。许多大型网站和服务都是用 Python 开发的，例如 YouTube、Dropbox、豆瓣等。以下是几种典型的 Web 框架：

- **Django**：一个高层次的 Python Web 框架，鼓励快速开发和简洁、实用的设计，是全栈框架的代表。
- **Flask**：一个轻量级的 Web 框架，强调简单性和灵活性，适合构建小型项目或微服务。

**系统运维** 

Python 是系统运维人员的必备语言。它可以用于编写脚本来自动化任务、管理服务器、处理文件和文本、与操作系统进行交互等。Python 的跨平台性使得它在不同的操作系统上都能有效发挥作用。

**金融** 

Python 在金融领域特别是量化交易和金融分析方面得到广泛应用。Python 的灵活性和丰富的金融数据分析库，使得它在金融工程领域的使用日益增多，重要性逐年提高。

**图形界面开发 (GUI)** 

Python 也可以用于开发桌面应用程序，以下是几种常用的图形界面开发库：

- **PyQt**：基于 Qt 框架的 Python 绑定，适合开发复杂的桌面应用程序。
- **WxPython**：基于 wxWidgets 的 Python GUI 库，提供了跨平台的原生控件。
- **TkInter**：Python 的标准 GUI 库，适合初学者和轻量级应用的快速开发。

## Python实际应用

**谷歌**：Google App Engine、code.google.com、Google Earth、谷歌爬虫、Google 广告等项目都在大量使用 Python 开发。

**CIA**：美国中情局网站就是用 Python 开发的。

**NASA**：美国航天局（NASA）大量使用 Python 进行数据分析和运算。

**YouTube**：世界上最大的视频网站 YouTube 就是用 Python 开发的。

**Dropbox**：美国最大的在线云存储网站，全部用 Python 实现，每天网站处理 10 亿个文件的上传和下载。

**Instagram**：美国最大的图片分享社交网站，每天超过 3000 万张照片被分享，全部用 Python 开发的。

**Facebook**：大量的基础库均通过 Python 实现的。

**Redhat**：世界上最流行的 Linux 发行版本中的 yum 包管理工具就是用 Python 开发的。

**豆瓣**：公司几乎所有的业务均是通过 Python 开发的。

**知乎**：国内最大的问答社区，通过 Python 开发（国外 Quora）。

除上面之外，还有搜狐、金山、腾讯、盛大、网易、百度、阿里、淘宝、土豆、新浪、果壳等公司都在使用 Python 完成各种各样的任务

## Python设计哲学

<img src="/static/notes_picture/python/python基础/image-20240902110217569.png" alt="image-20240902110217569" style="zoom:80%;" />

Python 的设计哲学与其他编程语言相比，有几个显著的不同之处：

1. **可读性优先**：
   - Python 强调代码的可读性，力求清晰明了。这与如 C++ 或 Java 等语言相比，后者往往更关注性能或复杂的语法结构。
2. **简洁性**：
   - Python 鼓励用较少的代码实现功能，通常会有简化的语法，而像 Java 这样的语言则要求更多的样板代码。
3. **动态类型**：
   - Python 是动态类型语言，变量类型在运行时决定，这与静态类型语言（如 C# 和 Java）形成鲜明对比，后者在编译时必须声明变量类型。
4. **多范式支持**：
   - Python 支持多种编程范式（如面向对象、函数式编程），而一些语言则更倾向于某一特定范式，如 Java 主要是面向对象的。
5. **强大的标准库**：
   - Python 附带了一个丰富的标准库，提供了大量现成的模块和功能，而其他语言可能需要依赖外部库或框架。
6. **社区和文化**：
   - Python 拥有一个积极的社区，强调开放和共享，鼓励用户贡献代码和文档，而其他语言的社区文化可能更加保守或封闭。

# Python环境部署

## Python解释器

- 打开官网：https://www.python.org/downloads
- 找到对应的版本，这里选择版本3.9.8

**3.9.8版本**下载链接：https://www.python.org/ftp/python/3.9.8/python-3.9.8-amd64.exe

<img src="/static/notes_picture/python/python基础/image-20240902111134272.png" alt="image-20240902111134272" style="zoom:80%;" />

<img src="/static/notes_picture/python/python基础/image-20240902111545070.png" alt="image-20240902111545070" style="zoom:80%;" />

打开安装包，添加环境变量，可以选择默认安装或者自定义安装（一般自定义安装主要是修改安装路径）

<img src="/static/notes_picture/python/python基础/image-20240902112236819.png" alt="image-20240902112236819" style="zoom:80%;" />

<img src="/static/notes_picture/python/python基础/image-20240902142136568.png" alt="image-20240902142136568" style="zoom:80%;" />

**注意：**必须勾选上下面的"Add Python 3.9 to PATH"(添加到系统环境变量中)

**测试是否安装成功**

在键盘上按下`win+R`然后在左下弹出窗口中输入`cmd`回车

在cmd终端中输入python，如果可以看到如下内容，说明python环境安装成功，并且请核对版本号是否与我们安装的一致....

```bash
C:\Users\test>python
Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Python编辑器

Python可用的编辑器有很多，因为编辑器只负责编写代码，实际的代码执行还是由我们刚刚安装的解释器进行编译解释。所以编写Python代码对编辑器的要求不是很高。不过，为了便于我们敲代码，我们还是要选择一些更加高级，功能更多的编辑器来使用。这样在编写代码的时候可以事半功倍

对于Python而言，最出名，最好用的编辑器就是pycharm了。我们后续学习也主要使用pycharm编辑器。

### 其他编辑器

**以下仅作为了解即可...**

1. **vim编辑器**

Vim（Vi IMproved）是一个高度可配置的文本编辑器，它源自于一个名为Vi的早期Unix编辑器。Vim的设计目标是提供一种高效的方式来编辑文本文件，它广泛应用于程序员和系统管理员中，因为它支持多种编程语言的语法高亮、代码补全、编译和错误跳转等功能。

Vim是一个主要基于命令行的编辑器，几乎所有的操作，如：复制、粘贴、删除等待，都需要通过指令来完成。所以说使用难度相对较高，我们后面的云计算部分会深入学习...

2. **Sublim Text**

Sublime Text 是一个代码编辑器（Sublime Text 2是收费软件，但可以无限期试用）

Sublime Text是由程序员Jon Skinner于2008年1月份所开发出来，它最初被设计为一个具有丰富扩展功能的Vim。

Sublime Text具有漂亮的用户界面和强大的功能，例如代码缩略图，Python的插件，代码段等。

还可自定义键绑定，菜单和工具栏。Sublime Text 的主要功能包括：拼写检查，书签，完整的 Python API ， Goto 功能，即时项目切换，多选择，多窗口等等。

Sublime Text 是一个跨平台的编辑器，同时支持Windows、Linux、Mac OS X等操作系统。

下载地址：http://www.sublimetext.com/3

<img src="/static/notes_picture/python/python基础/image-20240904101732444.png" alt="image-20240904101732444" style="zoom: 80%;" />

<img src="/static/notes_picture/python/python基础/image-20240902143634827.png" alt="image-20240902143634827" style="zoom:80%;" />

### Pycharm的安装

下载地址：http://www.jetbrains.com/pycharm/download/#section=windows

因为社区版可能会缺少部分功能，所以直接选择专业版

**安装过程：**

1. 下载安装包并且安装
2. 使用提供的补丁工具进行激活
3. 查看设置-->About

<img src="/static/notes_picture/python/python基础/image-20240902145526575.png" alt="image-20240902145526575" style="zoom:80%;" />

## 创建第一个项目

1. 点击New Project来创建一个项目，项目Name和Location可以自定义

<img src="/static/notes_picture/python/python基础/image-20240902145711220.png" alt="image-20240902145711220" style="zoom:80%;" />

2. 在项目名称上右键来创建一个Python File

<img src="/static/notes_picture/python/python基础/image-20240902145939086.png" alt="image-20240902145939086" style="zoom: 80%;" />

3. 编写第一个Python代码

```python
print('Hello World!')
```

然后右键->Run demo.py来运行

<img src="/static/notes_picture/python/python基础/image-20240902150205122.png" alt="image-20240902150205122" style="zoom:80%;" />

```bash
# Output
C:\Users\test\PycharmProjects\pythonProject\.venv\Scripts\python.exe C:\Users\test\PycharmProjects\pythonProject\demo.py 
hello world

Process finished with exit code 0
```

## Pycharm优化

1. 中文支持
2. 字体大小调节
3. 主题更改

......

# 02.Python基础语法.md

# 注释

单行注释：

```python
# 这是一条注释信息
```

多行注释：ctrl+/

三引号是将代码作为字符串处理

```python
'''
这是多行注释
'''
```

```python
"""
这是多行注释
"""
```

# 变量

什么是变量？

变量就是把某些值或者运行的结果临时保存在内存中，以便后续调用

## 强类型与弱类型

### 强类型（Strongly Typed）

- **定义**：在强类型语言中，类型检查在编译时或运行时都很严格，变量的类型在定义时明确，且不允许隐式转换。
- 特征：
  - 不同类型之间的操作会导致错误。
  - 类型安全，高度限制了类型不兼容的操作。
- **示例语言**：Java、C++、Python、Rust

**示例：python**

```python
a = 10
b = "10"
print(a+b)
print(a == b)

# Output:
TypeError: unsupported operand type(s) for +: 'int' and 'str'
......
```

只有数字字符可以直接与int类型互相转换,字母字符会报错

```python
a = '123'
b = int(a)
print(b)

#123
```

### 弱类型（Weakly Typed）

- **定义**：在弱类型语言中，变量的数据类型可以在运行时发生变化，允许隐式转换。
- 特征：
  - 不同类型之间的操作可能会被自动转换。
  - 灵活性高，但可能导致运行时错误或意外结果。
- **示例语言**：JavaScript、PHP、Ruby

**示例：JavaScript**

```python
let a = "5";
let b = 10;
let result = a + b; // result 为 "510"（字符串拼接）
```

## 动态类型与静态类型

### 动态类型（Dynamically Typed）

- **定义**：动态类型语言在运行时确定变量的类型，变量可以在程序执行过程中改变其类型。
- 特征：
  - 变量不需要在声明时指定类型。
  - 类型检查在运行时进行。
  - 允许在同一变量中存储不同类型的数据。
- **示例语言**：JavaScript、Python、Ruby、PHP。

**示例：python**

```python
a = 10      # 整数类型
print(a)    # 输出: 10

a = "Hello" # 现在是字符串类型
print(a)    # 输出: Hello
```

### 静态类型（Statically Typed）

- **定义**：静态类型语言在编译时确定变量的类型，变量的类型在声明时明确且在整个生命周期内保持不变。
- 特征：
  - 变量必须在声明时指定类型。
  - 类型检查在编译时进行。
  - 不允许在同一变量中存储不同类型的数据。
- **示例语言**：Java、C、C++、Go、Rust。

**示例：C语言**

```c
#include <stdio.h>

int main() {
    int a = 10;           // 整数类型
    float b = 5.5;       // 浮点类型
    char c = 'A';        // 字符类型

    printf("a = %d\n", a);
    printf("b = %.2f\n", b);
    printf("c = %c\n", c);

    return 0;
}
```

### 对比

| 特性     | 强类型               | 弱类型               |
| :------- | :------------------- | :------------------- |
| 类型检查 | 严格                 | 灵活                 |
| 隐式转换 | 不允许               | 允许                 |
| 错误检测 | 通常在编译时或运行时 | 可能在运行时发现错误 |
| 类型安全 | 高                   | 低                   |

## 声明变量

```python
a = "Hello World!"
print(a)
```

## 变量命名约定

### Python变量命名规则

- 变量名只能由字母、数字和下划线组成
- 变量名只能以字母或下划线开头，不能以数字开头
- 变量名不区分大小写，但为了提高可读性，推荐使用小写字母命名，并用下划线分隔多个单词
- 变量名不能使用Python的关键字，如下：
  - **['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']**
- 变量名应该具有描述性，以便能够清晰地表达变量的含义

### 常见的命名方式

1. 大驼峰命名法（Camel case）
   驼峰命名法是将多个单词连接在一起，每个单词首字母大写，这种命名方式常用于类、函数和对象的命名。

```python
FirstName = 'l'
LastName = 'xy'

print("你的名字是:",FirstName + LastName)
```

2. 下划线命名法（Snake case）
   下划线命名法是将多个单词连接在一起，使用下划线（_）分隔每个单词，所有字母小写。这种命名方式常用于变量和模块名的命名。

```python
first_str = 'Hello'
second_str = 'Python'

print(first_str + " " + second_str)
```

3. 全大写命名法（Pascal case / UPPERCASE）
   全大写命名法是将多个单词连接在一起，每个单词所有字母大写，可以加上适当的分隔符如下划线。这种命名方式常用于常量或全局变量的命名。

```python
FIRST_STR = 'Hello'
SECOND_STR = 'Python'

print( FIRST_STR+ " " + SECOND_STR)
```

类名：大驼峰命名法

函数：小驼峰

变量：下划线

常量（不应改变的）：全大写



## 变量的赋值

将某个数据赋值给某个变量存储

```python
a = "变量1"
b = "变量2"
```

 ![img](02.Python%E5%9F%BA%E7%A1%80%E8%AF%AD%E6%B3%95/1140672815.png) 

```python
a = "变量1"
b = a
```

 ![img](02.Python%E5%9F%BA%E7%A1%80%E8%AF%AD%E6%B3%95/4238420988.png) 

## 常量

常量是指在程序运行过程中其值不应被改变的变量。虽然 Python 本身并没有内置的常量类型，但有一些约定和方法可以用于定义常量。

### **定义常量：**

常量通常是通过使用大写字母命名的变量来表示。这是一种约定，表明该变量不应被修改。例如：

```python
PI = 3.14159
MAX_CONNECTIONS = 100
```

Python 没有内置的常量机制，但通过命名约定和模块结构，可以有效地使用常量来提高代码的可读性和可维护性。在设计大型程序时，合理使用常量是一个良好的编程习惯。

# 用户交互

## INPUT(输入)

**基本用法：**

```python
name = input('请输出你的姓名:')
print(name)
```

解释器在执行该代码的时候，如果遇到input就会出现阻塞，程序暂停，等待用户输入。当用户回车以后，程序才会继续向下执行

**注意：**通过**input函数**输入进来的内容一律会被当成**字符串**处理

```python
a = input('请输入一个数字:')
print(type(a))
print(a > 0)

# Output:
请输入一个数字:10
<class 'str'>
Traceback (most recent call last):
  File "D:\Code\Code\Python\PythonProject\测试\deom1.py", line 3, in <module>
    print(a > 0)
TypeError: '>' not supported between instances of 'str' and 'int'
```

如果想要规定**input**输入的类型，需要做类型转换，如下所示：

```python
a = int(input('请输入一个数字:'))
print(type(a))
print(a > 0)

# Output:
请输入一个数字:10
<class 'int'>
True
```

**其他用法：**

既然我们了解了input函数的特性，那么我们可以借助input函数来实现我们常见到的"按任意键结束......."

示例：

```python
import time
a = 12345
b = 54321
print("开始计算a的b次方")
a1 = a**b
print("开始计算b的a次方")
b1 = b**a
print("开始比较大小")
time.sleep(5)
print(a1 > b1)
input("比较结束，请按任意键回车结束.....")
```

## OUTPUT(输出)

**基本用法：**

```python
a = "Hello world"
print(a)
```

### 格式化输出

多行使用三引号

```python
name = input("姓名：")
age = input("年龄：")
job = input("工作：")
info = '''
----------- info of %s -----------
姓名：%s
年龄：%s
工作：%s
''' % (name,name,age,job)
print(info)
```

运行结果：

```python
姓名：lxy
年龄：18
工作：teacher

----------- info of lxy -----------
姓名：lxy
年龄：18
工作：teacher
```

### 字符串格式化标志(占位符)

以下是 Python 中字符串格式化的常见格式化标志及其说明：

- **`s`**：获取传入对象的 `__str__` 方法的返回值，并将其格式化到指定位置。
  
- **`r`**：获取传入对象的 `__repr__` 方法的返回值，并将其格式化到指定位置。

- **`c`**：
  - 整数：将数字转换成其 Unicode 对应的值（范围：0 <= i <= 1114111）。
  - 字符：将字符添加到指定位置。

- **`o`**：将整数转换成八进制表示，并将其格式化到指定位置。

- **`x`**：将整数转换成十六进制表示，并将其格式化到指定位置。

- **`d`**：将整数、浮点数转换成十进制表示，并将其格式化到指定位置。

- **`e`**：将整数、浮点数转换成科学计数法（小写 e），并将其格式化到指定位置。

- **`E`**：将整数、浮点数转换成科学计数法（大写 E），并将其格式化到指定位置。

- **`f`**：将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后 6 位）。

- **`F`**：同上。

- **`g`**：自动调整，将整数、浮点数转换成浮点型或科学计数法表示（超过 6 位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是 e）。

- **`G`**：自动调整，将整数、浮点数转换成浮点型或科学计数法表示（超过 6 位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是 E）。

- **`%`**：当字符串中存在格式化标志时，需要用 `%%` 表示一个百分号。

**示例：**

```python
# s：获取对象的 __str__ 方法返回值
name = "Alice"
print("Hello, %s!" % name)  # 输出: Hello, Alice!

# r：获取对象的 __repr__ 方法返回值
print("Name: %r" % name)  # 输出: Name: 'Alice'

# c：整数转换为其 Unicode 字符（0-1114111）
print("Unicode character: %c" % 65)  # 输出: Unicode character: A

# o：将整数转换为八进制表示
num = 10
print("Octal: %o" % num)  # 输出: Octal: 12

# x：将整数转换为十六进制表示
num = 255
print("Hexadecimal: %x" % num)  # 输出: Hexadecimal: ff

# d：将整数或浮点数转换为十进制表示
num = 42
print("Decimal: %d" % num)  # 输出: Decimal: 42

# e：将整数或浮点数转换为科学计数法（小写 e）
num = 123456789
print("Scientific: %e" % num)  # 输出: Scientific: 1.234568e+08

# E：将整数或浮点数转换为科学计数法（大写 E）
print("Scientific: %E" % num)  # 输出: Scientific: 1.234568E+08

# f：将整数或浮点数转换为浮点数表示，默认保留小数点后 6 位
num = 3.14159
print("Float: %f" % num)  # 输出: Float: 3.141590

# F：同上
print("Float: %F" % num)  # 输出: Float: 3.141590

# g：自动调整为浮点型或科学计数法，超出 6 位数使用科学计数法
num = 1234567.89
print("Auto: %g" % num)  # 输出: Auto: 1234567.89

# G：同上，但科学计数法用大写 E
print("Auto: %G" % num)  # 输出: Auto: 1234567.89

# %：表示一个百分号
percentage = 0.75
print("Percentage: %.2f%%" % (percentage * 100))  # 输出: Percentage: 75.00%
```

# 基本数据类型

## 整数(int)

- **描述：**表示没有小数部分的数字，可以是正数、负数或零。
- **特性：**
  - Python 3 中的 `int` 类型是无限大小的。这意味着你可以创建非常大的整数，而不必担心溢出（overflow）的问题。
  - Python 会根据整数的大小自动调整内存使用，因此可以存储任意大小的整数，只要计算机的内存允许。
  - 支持基本的算术运算，如加、减、乘、除等。

**示例：**

```python
a = 10
b = -5
c = 0
print(a + b)
# Output: 5
```

可以使用type()内置函数来查看某个变量或值的数据类型

```python
a = 2**64
print(type(a))    # type()是查看数据类型的方法
b = 2**60
print(type(b))

# Output:
<class 'int'>
<class 'int'>
```

## 字符串(str)

- **描述：**字符串是字符的序列，可以通过单引号或双引号定义。
- **特性：**
  - 字符串是**不可变**的（immutable），不能更改其内容。
  - 支持切片、连接、重复等操作。
  - 可以使用转义字符处理特殊字符。

在 Python 中, 加了引号的字符都被认为是字符串！

**示例：**

```python
Greeting = "Welcome to hhh"
Name = "lxy"
print(Greeting + " " + Name)	# 字符串可以通过+号进行拼接

# Output:
Welcome to hhh lxy
```

### 字符串的索引与切片

**字符串的索引：**

索引：每个字符在字符串中都有一个唯一的索引，索引从 `0` 开始。

负索引：可以使用负数索引从字符串的末尾开始访问字符，`-1` 表示最后一个字符，`-2` 表示倒数第二个字符，以此类推。

**示例：**

```bash
s = "Hello, World!"

# 正索引
print(s[0])  # 输出: H
print(s[7])  # 输出: W

# 负索引
print(s[-1])  # 输出: !
print(s[-5])  # 输出: W
```

**字符串的切片：**

切片：可以通过指定起始索引和结束索引来提取字符串的子串。切片的语法为 `s[start:end]`，包含起始索引的字符，但**不包含结束**索引的字符。

步长：可以指定步长来控制切片的间隔，语法为 `s[start:end:step]`。如果不指定步长，默认为 `1`。

**示例：**

```python
s = "Hello, World!"

# 基本切片
print(s[0:5])  # 输出: Hello
print(s[7:12])  # 输出: World

# 省略起始或结束索引
print(s[:5])  # 输出: Hello (从开始到索引 4)
print(s[7:])  # 输出: World! (从索引 7 到结束)

# 使用负索引切片
print(s[-6:-1])  # 输出: World

# 步长切片
print(s[::2])  # 输出: Hlo ol! (每隔一个字符)
print(s[::-1])  # 输出: !dlroW ,olleH (反转字符串)
```

### 字符串常用方法

```bash
# 字符串操作示例

words = "beautiful is better than ugly."

# 字符串的基本操作
print(words.capitalize())   # 首字母大写
print(words.swapcase())     # 大小写翻转
print(words.title())        # 每个单词的首字母大写

# 内容居中，总长度，空白处填充
a = "test"
ret = a.center(20, "*")
print(ret)

# 统计字符串中的元素出现的个数
ret = words.count("e", 0, 30)
print(ret)

# startswith 和 endswith 判断
print(a.startswith("a"))             # 判断是否以 'a' 开头
print(a.endswith("j"))               # 判断是否以 'j' 结尾
print(a.startswith('sdj', 2, 5))     # 判断子串是否在指定范围内
print(a.endswith('ado', 7, 10))      # 判断子串是否在指定范围内

# 寻找字符串中的元素是否存在
print(a.find('sdj', 1, 10))          # 返回索引，找不到返回 -1
print(a.index('sdj', 1, 10))         # 返回索引，找不到抛出异常

# split 以指定字符分割，形成列表
ret = words.split(' ')
print(ret)
ret = words.rsplit(' ', 2)           # 指定分割次数
print(ret)

# format 的三种用法
print('{} {} {}'.format('aaron', 18, 'teacher'))
print('{1} {0} {1}'.format('aaron', 18, 'teacher'))
print('{name} {age} {job}'.format(job='teacher', name='aaron', age=18))

# strip 操作
a = '****asdasdasd********'
print(a.strip('*'))   # 去除两端指定字符
print(a.lstrip('*'))  # 去除左侧指定字符
print(a.rstrip('*'))  # 去除右侧指定字符

# replace 操作
print(words.replace('e', 'a', 2))  # 替换 'e' 为 'a'，替换两次

# 字符串类型检查
print(words.isalnum())  # 判断字符串是否只由字母或数字组成
print(words.isalpha())   # 判断字符串是否只由字母组成
print(words.isdigit())   # 判断字符串是否只由数字组成
```

## 布尔类型(bool)

- **描述：**布尔类型只有两个值：`True` 和 `False`。
- **特性：**
  - 通常用于条件判断和逻辑运算。
  - 布尔值在逻辑表达式中可以进行运算。

布尔类型很简单，就两个值 ，一个 True(真)，一个 False(假), 主要用记逻辑判断

示例：

```python
a = 3
b = 5
print(a < b, a > b , a != b)

# Output:
True False True
```

# 基本运算符

## 算数运算符

用于执行基本的数学运算

| 运算符 | 描述                                               | 示例            |
| :----- | :------------------------------------------------- | :-------------- |
| `+`    | 加法，返回两个数的和                               | `3 + 5` → `8`   |
| `-`    | 减法，返回第一个数减去第二个数的结果               | `10 - 4` → `6`  |
| `*`    | 乘法，返回两个数的乘积                             | `2 * 3` → `6`   |
| `/`    | 除法，返回第一个数除以第二个数的结果，结果为浮点数 | `7 / 2` → `3.5` |
| `//`   | 地板除法，返回两个数相除的整数部分                 | `7 // 2` → `3`  |
| `%`    | 取模，返回第一个数除以第二个数的余数               | `7 % 2` → `1`   |
| `**`   | 幂运算，返回第一个数的第二个数次幂                 | `2 ** 3` → `8`  |

## 关系运算符

用于比较两个值的关系

| 运算符 | 描述                                     | 示例              |
| :----- | :--------------------------------------- | :---------------- |
| `==`   | 等于，判断两个值是否相等                 | `5 == 5` → `True` |
| `!=`   | 不等于，判断两个值是否不相等             | `5 != 3` → `True` |
| `>`    | 大于，判断左侧值是否大于右侧值           | `5 > 3` → `True`  |
| `<`    | 小于，判断左侧值是否小于右侧值           | `5 < 3` → `False` |
| `>=`   | 大于等于，判断左侧值是否大于或等于右侧值 | `5 >= 5` → `True` |
| `<=`   | 小于等于，判断左侧值是否小于或等于右侧值 | `3 <= 5` → `True` |

## 逻辑运算符

用于进行布尔逻辑运算

| 运算符 | 描述                                            | 示例                       |
| :----- | :---------------------------------------------- | :------------------------- |
| `and`  | 逻辑与，当且仅当两个表达式都为 True 时返回 True | `True and False` → `False` |
| `or`   | 逻辑或，只要有一个表达式为 True 即返回 True     | `True or False` → `True`   |
| `not`  | 逻辑非，返回布尔值的反转                        | `not True` → `False`       |

## 赋值运算符

用于给变量赋值

| 运算符 | 描述                              | 示例      |
| :----- | :-------------------------------- | :-------- |
| `=`    | 赋值，将右侧的值赋给左侧的变量    | `x = 5`   |
| `+=`   | 加法赋值，等同于 `x = x + 5`      | `x += 3`  |
| `-=`   | 减法赋值，等同于 `x = x - 5`      | `x -= 2`  |
| `*=`   | 乘法赋值，等同于 `x = x * 5`      | `x *= 4`  |
| `/=`   | 除法赋值，等同于 `x = x / 5`      | `x /= 2`  |
| `//=`  | 地板除法赋值，等同于 `x = x // 5` | `x //= 3` |
| `%=`   | 取模赋值，等同于 `x = x % 5`      | `x %= 2`  |
| `**=`  | 幂赋值，等同于 `x = x ** 5`       | `x **= 3` |

## 位运算符

用于对整数的二进制位进行操作

| 运算符 | 描述                                | 示例                                  |
| :----- | :---------------------------------- | :------------------------------------ |
| `&`    | 按位与，两个比特位都为 1 时结果为 1 | `5 & 3` → `1`                         |
| `      | `                                   | 按位或，只要有一个比特位为 1 结果为 1 |
| `^`    | 按位异或，当比特位不同结果为 1      | `5 ^ 3` → `6`                         |
| `~`    | 按位取反，反转所有比特位            | `~5` → `-6`                           |
| `<<`   | 左移运算，向左移动指定的比特位数    | `5 << 1` → `10`                       |
| `>>`   | 右移运算，向右移动指定的比特位数    | `5 >> 1` → `2`                        |

## 身份运算符

用于比较两个对象的内存地址

| 运算符   | 描述                         | 示例         |
| :------- | :--------------------------- | :----------- |
| `is`     | 判断两个对象是否为同一对象   | `x is y`     |
| `is not` | 判断两个对象是否不是同一对象 | `x is not y` |

## 成员运算符

用于检查值是否在序列中

| 运算符   | 描述                   | 示例                          |
| :------- | :--------------------- | :---------------------------- |
| `in`     | 判断元素是否在序列中   | `3 in [1, 2, 3]` → `True`     |
| `not in` | 判断元素是否不在序列中 | `4 not in [1, 2, 3]` → `True` |

## 运算符优先级

以下表格列出了从最高到最低优先级的所有运算符：

| 优先级 | 运算符                                     | 描述                       |
| :----- | :----------------------------------------- | :------------------------- |
| 1      | `()`                                       | 括号，改变运算顺序         |
| 2      | `**`                                       | 幂运算                     |
| 3      | `+`, `-`                                   | 正负号（正负运算）         |
| 4      | `*`, `/`, `//`, `%`                        | 乘法、除法、地板除法、取模 |
| 5      | `+`, `-`                                   | 加法、减法                 |
| 6      | `<<`, `>>`                                 | 位移运算                   |
| 7      | `&`                                        | 按位与                     |
| 8      | `^`                                        | 按位异或                   |
| 9      | `                                          | `                          |
| 10     | `==`, `!=`, `>`, `<`, `>=`, `<=`           | 比较运算                   |
| 11     | `is`, `is not`, `in`, `not in`             | 身份和成员运算             |
| 12     | `not`                                      | 逻辑非                     |
| 13     | `and`                                      | 逻辑与                     |
| 14     | `or`                                       | 逻辑或                     |
| 15     | `=`                                        | 赋值                       |
| 16     | `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` | 赋值运算                   |

### 注意事项

1. **括号优先**：使用括号可以改变运算顺序，任何在括号内的运算会优先计算。
2. **运算符结合性**：
   - 大多数运算符是从左到右结合的，例如加法和减法。
   - 幂运算 `**` 是从右到左结合，即 `2 ** 3 ** 2` 等于 `2 ** (3 ** 2)`。
3. **比较运算符**：比较运算符的优先级在逻辑运算符之前。
4. **赋值运算符**：赋值运算符的优先级最低。

**示例：**

```python
# 示例 1
result = 2 + 3 * 4  # 结果为 14，因为乘法优先于加法

# 示例 2
result = (2 + 3) * 4  # 结果为 20，因为括号改变了优先顺序

# 示例 3
result = 2 ** 3 ** 2  # 结果为 512，因为幂运算是右结合的
```

了解运算符优先级有助于在编写和阅读代码时清晰地理解表达式的计算顺序。


# 03.Python数据结构.md

# Python基本数据结构

# 列表(List)

列表是一个有序的可变集合，可以存储不同类型的元素。列表相比于字符串，不仅可以储存不同的数据类型，而且可以储存大量数据。而且列表是有序的，有索引值，可切片，方便取值。

## 定义列表

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Output:
['apple', 'banana', 'cherry']
```

## 增加元素

```python
# 1. 按照索引的位置去增加
fruits.insert(1, "kiwi")

# 2. 在最末尾添加
fruits.append("orange")

# 3. 用迭代的方式去添加
fruits.extend(['a','b','c'])		
# 可以立即为再传递一个List进去，然后依次添加到末尾,而append会把括号里的当成一个整体添加到末尾

# Output:
['apple', 'kiwi', 'banana', 'cherry', 'orange', 'a', 'b', 'c']
```

## 删除元素

```python
# 1. 删除制定的具体元素
fruits.remove("cherry")

# 2. 按照索引位置去删除
fruits.pop()		# 默认是删除最后一个，可以加上索引。并且有返回值，返回值为删除的元素
fruits.pop(1)

# 3. 使用切片范围删除
del fruits[1:3]		# 没有返回值

# 4. 清空列表
fruits.clear()

# 5. 删除列表
del fruits

# clear是清空列表的内容，变成一个空列表，而del是删除列表本身，后续无法再次调用...

# Output:
['apple', 'banana', 'cherry']
['apple', 'kiwi', 'banana', 'cherry', 'orange', 'a', 'b', 'c']
[]
```

## 修改元素

```python
# 1. 按照索引修改某个元素的值
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)

# Output:
['apple', 'orange', 'cherry']

# 2. 按照切片范围修改
fruits[0:2] = ['kiwi','orange']
print(fruits)

# Output:
['kiwi', 'orange', 'cherry']
```

## 查找元素

```python
# 1. index(element)：返回元素的索引
fruits = ["apple", "banana", "cherry"]
index_of_apple = fruits.index("apple")
print(index_of_apple)

# Output:
0

# 2. count(element)：返回元素出现的次数
count_of_cherry = fruits.count("cherry")
print(count_of_cherry)

# Output:
1
```

## 列表的切片

切片是按照一定的索引规律分割列表从而组成一个新的列表，类似与我们字符串中讲到的切片

```python
li = [1,2,4,5,4,2,4]
sub_li = li[2:5]
print(sub_li)

# Output:
[4, 5, 4]
```

## 其他操作

```python
li = [1,2,4,5,4,2,4]
# 1. 统计某个元素出现的次数
print (li.count(4))

# 2. 从列表中找出某个值第一个匹配项的索引位置
print (li.index(2))

# 3. 对列表进行排序
li.sort()
print(li)

# 4. 将列表中的元素反向存放
li.reverse()
print (li)

# Output:
3
1
[1, 2, 2, 4, 4, 4, 5]
[5, 4, 4, 4, 2, 2, 1]
```

# 元组(Tuple)

有序的**不可变**集合，也被被称为只读列表，即数据可以被查询，但不能被修改。

## 定义元组

```python
tuple = (1,2,3,'a','b','c')
print(tuple)
print(tuple[1])

# 可以删除元素吗?
tuple.pop()

# Output:
AttributeError: 'tuple' object has no attribute 'pop'
```

## 可变元组

tuple其实不可变的是地址空间，如果地址空间里存的是可变的数据类型的话，比如列表就是可变的

```python
tuple = (1, 2, 3, [1, 4, 7])
print(tuple)
tuple[3][2] = 100
print(tuple)

# Output:
(1, 2, 3, [1, 4, 7])
(1, 2, 3, [1, 4, 100])
```

在元组tuple中，包含一个list类型的数据，由于list是可以变的，所以我们可以更改元组里list的值，但是元组本身的地址空间是不变的。

<img src="/static/notes_picture/python/python基础/image-20240904095734746.png" alt="image-20240904095734746" style="zoom:80%;" />

# 字典(Dict)

字典是python中唯一的映射类型，采用键值对（key-value）的形式存储数据。python对key进行哈希函数运算，根据计算的结果决定value的存储地址，所以字典是无序存储的，且key必须是可哈希的。可哈希表示key必须是不可变类型，如：数字、字符串、元组。

不过在Python 3.6版本以后，字典会保留插入顺序，变成有序数据结构。

而且键是具有唯一性的，每个键只能出现一次，但是值没有限制，在一个字典中可以出现多个相同的值。

## 定义字典

```python
dic = {'name':'lxy','age':18,'job':'teacher'}
print(dic)
print(dic['name'])
print(dic['age'])
print(dic['job'])

# Output:
{'name': 'lxy', 'age': 18, 'job': 'teacher'}
nls
18
teacher
```

## 增加键值

```python
dic = {'name':'lxy','age':18,'job':'teacher'}

# 1. 直接通过键值对来增加
dic['hobby'] = 'study'		# 如果键已经存在，那么就会替换原来的值

print(dic)
# Output: {'name': 'lxy', 'age': 18, 'job': 'teacher', 'hobby': 'study'}

# 2. 在字典中添加键值对时，如果指定的键已经存在则不做任何操作,如果原字典中不存在指定的键值对，则会添加。
dic.setdefault('name','lxy')
dic.setdefault('gender','男')
print(dic)

# Output:
{'name': 'lxy', 'age': 18, 'job': 'teacher', 'hobby': 'study', 'gender': '男'}
```

## 删除键值

```python
dic = {'name':'lxy','age':18,'job':'teacher'}

# 1. 删除指定的键,并且返回对应的值
name = dic.pop('job')
hobby = dic.pop('hobby','查无此项')		# 可以在后面加上一个异常处理，如果key不存在，就输出后面的内容
print(dic)
print(name)
print(hobby)

# Output:
{'name': 'lxy', 'age': 18}
teacher
查无此项

# 2. 使用del关键字删除指定的键值对
del dic['name']

# 3. 删除最后插入的键值对
dic_pop = dic.popitem()
print(dic_pop)

# 4. 清空字典
dic.clear()
print(dic)

# Output: {}
```

## 修改键值

```python
dic = {'name':'lxy','age':18,'job':'teacher'}
dic['age'] = 25

print(dic)

# Output:
{'name': 'lxy', 'age': 25, 'job': 'teacher'}
```

## 查找键值

```python
dic = {'name':'lxy','age':18,'job':'teacher'}
# 1. 直接通过键名获取，如果不存在会报错
value = dic['name']
print(value)

# 2. 使用get方法获取键值,若不存在则返回 None，可以自定义异常返回值
value = dic.get('job','查无此项')
print(value)

# Output:
lxy
teacher

# 3. IN关键字，存在返回True，反之False
exists = "name" in dic
print(exists)

# Output:
True
```

## 其他操作

```python
dic = {'name':'lxy','age':18,"phone":['1888888888','0511-10101010']}
# 字典里面的value也可以是容器类型的数据，比如列表，字典等等...但是key必须是不可变的
print(dic)

# 1. 对键和值进行迭代操作
for i in dic.items():
	# 将键和值作为元祖列出
    print(i)

for i in dic:
	# 只迭代键
    print(i)
    
# Output:
('name', 'lxy')
('age', 18)
('phone', ['1888888888', '0511-10101010'])
name
age
phone

# 2. 使用keys()和values()方法获取键值
keys = dic.keys()
print(keys,type(keys))

value = dic.values()
print(value,type(value))

# Output:
dict_keys(['name', 'age', 'phone']) <class 'dict_keys'>
dict_values(['lxy', 18, ['1888888888', '0511-10101010']]) <class 'dict_values'>
```

# 集合(Set)

集合是**无序**的，**不重复**，**确定性**的数据集合，它里面的元素是可哈希的(不可变类型)，但是集合本身是不可哈希（所以集合做不了字典的键）的。以下是集合最重要的两点：

- 去重，把一个列表变成集合，就自动去重了。
- 关系测试，测试两组数据之前的交集、差集、并集等关系。

## 定义集合

```python
set1 = {1,2,3,'a','b','c'}		# 推荐方法
set2 = set({1,2,3})

print(set1, set2)

# Output:
{1, 2, 3, 'b', 'c', 'a'} {1, 2, 3}
```

## 增加元素

```python
set1 = {1,2,3,'a','b','c'}
# 1. 使用add()方法为集合增加元素
set1.add('d')
print(set1)

# Output:
{'a', 1, 2, 3, 'c', 'd', 'b'}

# 2. 使用update()方法迭代的去增加
set1.update('e','f')
# update接收的参数应该是可迭代的数据类型，比如字符串、元组、列表、集合、字典。这些都可以向集合中添加元素，但是整型、浮点型不可以
set1.update([4,5,6])
print(set1)

# Output:
{1, 2, 3, 4, 5, 6, 'a', 'd', 'b', 'c', 'f', 'e'}
```

## 删除元素

```python
set1 = {1,2,3,'a','b','c'}
# 1. 使用remove()方法删除元素
set1.remove('a')

print(set1)

# 2. 随机删除某个元素
set1.pop()
print(set1)

# Output:
{1, 2, 3, 'c', 'b'}
{2, 3, 'c', 'b'}

# 3. 删除集合本身
del set1
```

## 查找元素

```python
set1 = {1,2,3,'a','b','c'}
exists = "a" in set1  # True
print(exists)
```

## 关系测试

### 交集(& 或者 intersection)

取出两个集合共有的元素

```python
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 & set2)
print(set1.intersection(set2))

# Output:
{3, 4, 5}
{3, 4, 5}
```

### 反交集(^ 或者 symmetric_difference)

```python
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Output:
{1, 2, 6, 7}
{1, 2, 6, 7}
```

### 并集(| 或者 union)

合并两个集合的所有元素

```python
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 | set2)
print(set2.union(set1))

# Output:
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
```

### 差集(- 或者 difference)

第一个集合去除二者共有的元素

```python
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 - set2)
print(set1.difference(set2))

# Output:
{1, 2}
{1, 2}
```

### 子集与超集

当一个集合的所有元素都在另一个集合里，则称这个集合是另一个集合的子集，另一个集合是这个集合的超集

```python
set1 = {1,2,3}
set2 = {1,2,3,4,5,6}

print(set1 < set2)
print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

print(set2 > set1)
print(set2.issuperset(set1))  # 这两个相同，都是说明set2是set1超集
```

## 不可变集合

```python
set1 = {1,2,3,4,5,6}

set2 = frozenset(set1)
print(set2,type(set2))

set2.add(7) # 不可以修改,会报错

# Output:
AttributeError: 'frozenset' object has no attribute 'add'
```

# 数据结构的总结

| 数据结构              | 描述             | 特性                   | 常见操作               | 适用场景                                 | 优点                        | 缺点                                  |
| :-------------------- | :--------------- | :--------------------- | :--------------------- | :--------------------------------------- | :-------------------------- | :------------------------------------ |
| **列表 (List)**       | 有序的可变集合   | 有序、可变、支持重复   | 添加、删除、修改、查找 | 需要维护元素顺序的场景，如队列、栈的实现 | 灵活性高，支持多种操作      | 查询复杂度为 O(n)，插入和删除性能较差 |
| **元组 (Tuple)**      | 有序的不可变集合 | 有序、不可变、支持重复 | 查找                   | 元素不需要修改的场景，如函数参数、字典键 | 更节省内存，速度较快        | 不支持修改                            |
| **集合 (Set)**        | 无序的可变集合   | 无序、可变、不支持重复 | 添加、删除、查找       | 需要去重和快速查找的场景，如集合运算     | 快速查找和去重              | 不支持索引，元素无序                  |
| **字典 (Dictionary)** | 有序的键值对集合 | 有序、可变、键唯一     | 添加、删除、修改、查找 | 需要快速查找和存储键值对的场景，如缓存   | 快速查找（O(1) 平均复杂度） | 键必须是不可变类型，内存开销较大      |
| **字符串 (String)**   | 字符的序列       | 不可变                 | 查找、切片、替换       | 文本处理                                 | 易于使用，内置丰富的方法    | 不可修改，性能较低                    |

# 流程控制

## 判断语句(if)

**语法：**

```python
if 条件:
    满足条件后要执行的代码
```



<img src="/static/notes_picture/python/python基础/image-20240904142740373.png" alt="image-20240904142740373" style="zoom:80%;" />

### 单分支判断

```python
# 提示用户输入年龄
age = int(input("请输入你的年龄："))

# 单分支判断
if age >= 18:
    print("已经成年，可以去网吧上网了")
    print("欢迎来到Eagles网吧")

print("你还没成年，要好好学习")
```

### 双分支判断

```python
"""
if 条件:
    满足条件执行代码
else:
    if条件不满足就走这段
"""

# 提示用户输入年龄
age = int(input("请输入你的年龄："))

# 单分支判断
if age >= 18:
    print("已经成年，可以去网吧上网了")
    print("欢迎来到Eagles网吧")
else:
    print("你还没成年，要好好学习")
```

### 多分支判断

```python
if 条件:
    满足条件执行代码
elif 条件:
    上面的条件不满足就走这个
elif 条件:
    上面的条件不满足就走这个
elif 条件:
    上面的条件不满足就走这个    
else:
    上面所有的条件不满足就走这段


# 成绩判断程序
# 提示用户输入成绩
score = int(input("请输入成绩（0-100）："))

# 多分支判断成绩
if score >= 90 and score <= 100:
    print("优秀")
elif score >= 60 and score < 90:
    print("良好")
elif score >= 0 and score < 60:
    print("不及格")
else:
    print("输入错误，请输入0到100之间的成绩。")
```

## 循环语句-while

**语法：**

```python
while 条件:
     循环体
        
# 循环条件可以直接是True/False或者1/0，也可以是某个语句...
```

如果条件为真，那么循环体则执行 
如果条件为假，那么循环体不执行

**示例：猜数字小游戏**

```python
print('猜数字游戏开始')
num = 54
while True:
    guess = int(input("您猜数字是什么？(输入0-100的数字):"))
    if guess < num:
        print("您猜小了")
        continue
    elif guess > num:
        print("您猜大了")
        continue
    break

print("您猜对了！")

# Output:
猜数字游戏开始
您猜数字是什么？(输入0-100的数字):10
您猜小了
您猜数字是什么？(输入0-100的数字):50
您猜小了
您猜数字是什么？(输入0-100的数字):60
您猜大了
您猜数字是什么？(输入0-100的数字):54
您猜对了！
```

### 循环终止语句

#### break

用于完全结束一个循环，跳出循环体执行循环后面的语句

#### continue

和 break 有点类似，区别在于 continue 只是终止本次循环，接着还执行后面的循环，break 则完全终止循环

#### while...else结构

while 后面的 else 作用是指，当 while 循环正常执行完，中间没有被 break 中止的话，就会执行 else 后面的语句

- **语法：**

```python
while condition:
    # 循环体
    if some_condition:
        break
else:
    # 循环正常结束时执行的代码
```

- **示例：**

```python
# 寻找素数的示例
num = 10
i = 2

while i < num:
    if num % i == 0:
        print(f"{num} 不是素数，因为它可以被 {i} 整除。")
        break
    i += 1
else:
    print(f"{num} 是一个素数！")
```

## 循环语句-for

for循环：用户按照顺序循环可迭代对象的内容

**语法：**

```python
for variable in iterable:
    # 循环体
    # 执行的代码
```

### 遍历列表

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
# Output:
apple
banana
cherry
```

### 遍历字符串

```python
word = "helloworld"
for letter in word:
    print(letter)

# Output:
h
e
l
l
o
w
o
r
l
d
```

## enumerate

enumerate：枚举，对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值。

```python
li = ['甲','乙','丙','丁']
for i in enumerate(li):
    print(i)

for index,value in enumerate(li):
    print(index,value)

for index,value in enumerate(li,100): #从哪个数字开始索引
    print(index,value)
    
# Output:
(0, '甲')
(1, '乙')
(2, '丙')
(3, '丁')
0 甲
1 乙
2 丙
3 丁
100 甲
101 乙
102 丙
103 丁
```

## range

指定范围，生成指定数字

```bash
for i in range(1,10):
    print(i)
#1，2，....，9
for i in range(1,10,2):  # 步长
    print(i)

for i in range(10,1,-2): # 反向步长
    print(i)
```

### 小游戏案例

石头简单布

```bash
import random
# random产生随机值或者从给定值中随机选择

# 可选择的选项
options = ["石头", "剪子", "布"]

print("欢迎来到石头剪子布游戏！")
print("请从以下选项中选择：")
for i, option in enumerate(options):
    print(f"{i + 1}. {option}")

# 玩家选择
player_choice = int(input("请输入你的选择（1-3）：")) - 1

# 计算机随机选择
computer_choice = random.randint(0, 2)

print(f"\n你选择了：{options[player_choice]}")
print(f"计算机选择了：{options[computer_choice]}")

# 判断胜负
if player_choice == computer_choice:
    print("平局！")
elif (player_choice == 0 and computer_choice == 1) or \
     (player_choice == 1 and computer_choice == 2) or \
     (player_choice == 2 and computer_choice == 0):
    print("你赢了！🎉")
else:
    print("你输了！😢")
```

# 课后作业

## 完善猜数字小游戏

1. 生成一个随机数

2. 猜错3次了以后，程序自动退出...

## 完善石头剪刀布游戏

1. 更新游戏规则，实现三局两胜制
2. 胜利条件：
   - **2:1**
   - **3:0**



# 04.Python文件操作.md

# Python文件操作

在 Python 中，文件操作是非常常见的任务。Python 提供了内置的函数来处理文件的读写操作。

## 文件的类型

1. **文本文件**：包含可读的字符（如 `.txt`、`.csv`）。一般使用 UTF-8 编码，可以使用文本编辑器查看；
2. **二进制文件**：包含非文本数据（如图像、音频、视频文件，后缀如 `.jpg`、`.png`、`.mp3`）。以原始字节格式存储。需要使用专用软件查看；

## 文件操作的过程

1. 打开文件；

2. 读写文件；

   - 读文件：将文件内容读入内存；

   - 写文件：将内存内容写入文件；

3. 关闭文件；

# 操作方法

## 打开文件

使用 `open()` 函数打开文件

`open` 函数负责打开文件，并且返回文件对象

1. 第一个参数是文件名（文件名区分大小写），第二个参数是打开方式；
2. 如果文件存在返回文件操作对象；
3. 如果文件不存在抛出异常

```python
f = open("文件名", "访问方式")
```

### 文件路径

#### **绝对路径：**

从根路径开始描述文件的位置，例如：`F:\技术文件\课件-笔记\课件修订\Python\01.Python基础语法`

具有唯一性，不会出错，不管写在哪里都可以准确的找到文件的位置

#### **相对路径：**

相对当前位置进行文件定位，容易出错，需要对路径比较熟悉

### 以不同模式打开

| 访问方式 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| r        | 以**只读**方式打开文件。文件的指针将会放在文件的开头，这是**默认模式**。如果文件不存在，抛出异常 |
| w        | 以**只写**方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件 |
| a        | 以**追加**方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入 |
| r+       | 以**读写**方式打开文件。文件的指针将会放在文件的开头。如果文件不存在，抛出异常 |
| w+       | 以**读写**方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件 |
| a+       | 以**读写**方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入 |

以bytes类型操作的读写，写读，写读模式

| r+b  | 读写【可读，可写】 |
| :--- | :----------------- |
| w+b  | 写读【可写，可读】 |
| a+b  | 写读【可写，可读】 |

对于非文本文件，我们只能使用b模式，"b"表示以字节的方式操作（而所有文件也都是以字节的形式存储的，使用这种模式无需考虑文本文件的字符编码、图片文件的jgp格式、视频文件的avi格式）

<font color=red>注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型，不能指定编码</font>

### 文件编码

f=open(...)是由操作系统打开文件，那么如果我们没有为open指定编码，那么打开文件的默认编码很明显是操作系统说了算了，操作系统会用自己的默认编码去打开文件，在windows下是gbk，在linux下是utf-8。

```python
f=open('example.txt','r',encoding='utf-8')
```

## 读取文件

- **`read(size)`**：读取指定大小的内容，如果没有指定，读取全部内容。
- **`readline()`**：读取一行。
- **`readlines()`**：读取所有行并返回一个列表。

示例：

```python
file = open('example.txt', 'r')

content = file.read()  		# 读取全部内容
line = file.readline()  	# 读取一行
lines = file.readlines()  	# 读取所有行

print(content)
print('-----------')
print(line)
print('-----------')
print(lines)

# 思考?
# 为什么后面两个print读取不到东西呢？
```

### 文件指针 seek

有时候我们想要改变文件指针(光标)的位置，就需要用到seek方法来操作指针

**语法：**

```python
file.seek(offset, whence)
```

- **`offset`**：要移动的字节数。

- `whence`

  （可选）：指定偏移量的基准位置。可以取以下值：

  - `0`：从文件开头开始计算（默认值）。
  - `1`：从当前位置开始计算。
  - `2`：从文件末尾开始计算

**示例：**

```python
file = open('example.txt', 'r')

content = file.read()  		# 读取全部内容
file.seek(0)				# 把光标移到到文件的开头
line = file.readline()  	# 读取一行
file.seek(0)				# 再次把光标移动到文件的开头
lines = file.readlines()  	# 读取所有行

print(content)
print('-----------')
print(line)
print('-----------')
print(lines)
```

### 按行读取文件内容

- read方法默认会把文件的所有内容一次性读取到内存
- readline方法可以一次读取一行内容

```python
# 方式一、通过循环按行读取文件所有内容
file1 = open("example.txt")
i = 1
while True:
    text1 = file1.readline().strip()
    if text1:
        print("这是第%s行内容" % i)
        i += 1
        print(text1)
    else:
        break

file1.close()

file2 = open("example.txt")

# 通过for遍历按行读取文件所有内容
for i in file2.readlines():
    print(i.strip())

file2.close()
```

## 写入内容

可以对文件对象调用write方法实现写入内容

**语法：**

```python
file.write()
```

**示例：日记记录**

```python
# 日记程序
# 以追加模式打开日记文件
file = open('diary.txt', 'a',encoding='utf-8')

# 获取用户输入的日记内容
content = input("请输入今天的日记：")

# 将日记内容写入文件
file.write(content + "\n")
print("日记已保存！")

# 关闭文件
file.close()
```

## 关闭文件

**语法：**

```python
file.close()
```

使用 `close()` 方法关闭文件，释放系统资源,防止文件被一直占用

## with结构

使用 `with` 语句可以自动管理文件的打开和关闭，避免忘记关闭文件的情况。

```python
with open('example.txt', 'r') as file:		# 获取file文件对象
    content = file.read()
```

**案例：简单的备份程序**

将一个文本文件的内容复制到另一个文件，用于简单的备份。

```python
# 简单备份小程序
source = 'a.txt'
destination = 'b.txt'

with open(source, 'r',encoding='utf-8') as src:
    content = src.read()

with open(destination, 'w',encoding='utf-8') as dest:
    dest.write(content)

print(f"备份成功！'{source}' 的内容已复制到 '{destination}'")
```

## 其他文件操作

除了上述讲到的常用操作之外，还有很多其他的操作。这里我们列出在这，就不一一带着大家去看了。用到的时候可以回头来查一下就行

```python
class CustomFile:
    def __init__(self, *args, **kwargs):
        """初始化文件对象."""
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """创建并返回一个新的对象."""
        pass

    def close(self, *args, **kwargs):
        """关闭文件."""
        pass

    def fileno(self, *args, **kwargs):
        """返回文件描述符."""
        pass

    def flush(self, *args, **kwargs):
        """刷新文件内部缓冲区."""
        pass

    def isatty(self, *args, **kwargs):
        """判断文件是否是一个终端设备."""
        pass

    def read(self, *args, **kwargs):
        """读取指定字节的数据."""
        pass

    def readable(self, *args, **kwargs):
        """检查文件是否可读."""
        pass

    def readline(self, *args, **kwargs):
        """仅读取一行数据."""
        pass

    def seek(self, *args, **kwargs):
        """移动文件指针到指定位置."""
        pass

    def seekable(self, *args, **kwargs):
        """检查指针是否可操作."""
        pass

    def tell(self, *args, **kwargs):
        """获取当前指针位置."""
        pass

    def truncate(self, *args, **kwargs):
        """截断文件，仅保留指定之前的数据."""
        pass

    def writable(self, *args, **kwargs):
        """检查文件是否可写."""
        pass

    def write(self, *args, **kwargs):
        """写入内容到文件."""
        pass

    def __next__(self, *args, **kwargs):
        """实现迭代器的 next() 方法."""
        pass

    def __repr__(self, *args, **kwargs):
        """返回文件对象的字符串表示."""
        pass

    def __getstate__(self, *args, **kwargs):
        """自定义对象的序列化状态."""
        pass
```

### 解释

1. **`__init__`**: 初始化文件对象的方法。通常在这里设置文件的基本属性。
2. **`__new__`**: 静态方法，用于创建新的对象实例。
3. **`close`**: 关闭文件，释放系统资源。
4. **`fileno`**: 返回文件描述符，通常用于与底层操作系统交互。
5. **`flush`**: 刷新文件的内部缓冲区，将未写入的数据写入文件。
6. **`isatty`**: 判断文件是否是一个终端设备（tty），用于检查文件是否连接到一个用户界面。
7. **`read`**: 读取指定字节的数据，可以用来读取文件内容。
8. **`readable`**: 检查文件对象是否可读。
9. **`readline`**: 读取文件中的一行数据，常用于逐行读取文件内容。
10. **`seek`**: 移动文件指针到指定位置，允许在文件中随机访问。
11. **`seekable`**: 检查文件指针是否可操作，确定文件是否支持随机访问。
12. **`tell`**: 返回当前文件指针的位置。
13. **`truncate`**: 截断文件，只保留指定位置之前的数据。
14. **`writable`**: 检查文件对象是否可写。
15. **`write`**: 向文件写入内容。
16. **`__next__`**: 实现迭代器的 `next()` 方法，用于支持迭代访问文件的内容。
17. **`__repr__`**: 返回文件对象的字符串表示，通常用于调试。
18. **`__getstate__`**: 自定义对象的序列化状态，用于存储和恢复对象的状态。

# 案例练习

## 案例一 文件修改

文件的数据是存放于硬盘上的，因而只存在覆盖、不存在修改这么一说，我们平时看到的修改文件，都是模拟出来的效果，具体的说有两种实现方式：

方式一：将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）

```python
import os

with open('a.txt') as read_f,open('a.txt.new','w') as write_f:
    data = read_f.read()
    data = data.replace('Hello','nihao')

    write_f.write(data)

os.remove('a.txt')
os.rename('a.txt.new','a.txt')
```

方式二：将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件

```python
import os

with open('a.txt') as read_f,open('a.txt.new','w') as write_f:
    for line in read_f:
        line = line.replace('nihao','Hello')
        write_f.write(line)

os.remove('a.txt')
os.rename('a.txt.new','a.txt')
```

## 案例二 商品信息管理与总价计算

#### 背景

在日常的商业管理中，商品的管理和销售记录是非常重要的。我们需要一种方式来处理商品信息，包括商品名称、价格和数量。通过这些信息，我们可以计算出总价，帮助商家了解销售情况。

#### 目标

本案例旨在通过 Python 读取存储在文本文件中的商品信息，并将其转换为易于操作的数据结构。具体目标包括：

1. 从文件 `a.txt` 中读取每一行的商品信息。
2. 将读取的信息构建为包含字典的列表，每个字典表示一个商品，包含名称、价格和数量。
3. 计算所有商品的总价，并输出结果。

#### 文件内容示例

`a.txt` 文件的内容如下：

```
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3
```

每行代表一个商品，格式为：`商品名称 价格 数量`。

#### 代码示例

```python
# 初始化商品列表
products = []

# 读取文件并构建商品列表
with open('a.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 去除行首尾空白并分割
        parts = line.strip().split()
        if len(parts) == 3:  # 确保有三个部分
            product = {
                'name': parts[0],
                'price': int(parts[1]),  # 转换为整数
                'amount': int(parts[2])   # 转换为整数
            }
            products.append(product)

# 输出商品列表
print("商品列表", products)

total_price = 0
# 计算总价
for i in products:
    total_price += i[1] * i[2]

# 输出总价
print("总价:", total_price)

# Output:
[{'name': 'apple', 'price': 10, 'amount': 3}, {'name': 'tesla', 'price': 100000, 'amount': 1}, {'name': 'mac', 'price': 3000, 'amount': 2}, {'name': 'lenovo', 'price': 30000, 'amount': 3}, {'name': 'chicken', 'price': 10, 'amount': 3}]
总价: 196060
```

## 案例三 基于文件的账户验证

将用户信息存放在文件**user.txt**中，并且格式如下

```
张三|123456
```

**代码示例：**

```python
db = {}
with open("user.txt","r", encoding="utf-8") as f:
    data = f.readlines()
    print(data)
    for i in data:
        ret = i.strip().split("|")
        # ret = ["张三", "123"]
        print(ret)
        db[ret[0]] = ret[1]
        # db["张三"] = "123"
        print(db)

while True:
    username = input("请输入用户名：")

    if username in db:
        password = input("请输入密码：")
        if password ==db[username]:
            print("登录成功")
        else:
            print("密码错误登录失败")
    else:
        print("用户名不存在")
```

# 课后作业

```
1. 完成上述几个案例
2. 扩展案例三 基于文件的账户验证。为其增加注册功能并且让整个代码更加合理
3. 尝试一下实现密码错误3次封号的功能
```



