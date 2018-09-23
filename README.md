# watchguard

功能描述：
    
    1、从如下网站获取Firebox T/M series 下的各个型号
    https://www.watchguard.com/wgrd-products/appliances-compare
    2、选择获取的型号，进行比较
    3、提取比较结果中各型号的Performance的性能指标的数据
    4、性能数据以”Firewall Throughput”从小到大排序，并存储为csv文件
    
解决方案
    
     1、使用selenium 对chrome浏览器进行操作，通过型号框的xpath获取型号数据
     2、通过行号获取性能数据，以pd.DataFrame形式返回
     3、带单位的数据排序，采用提取pd.DataFrame排序列，统一单位，插入排序列到pd.DataFrame,再
        利用该实例自带的排序功能进行排序，提取需要的排序数据
     4、利用pd.DataFrame自带方法，存为csv文件
     
模块设计

    1、采用3层独立的模块设计方法：
        lib层：底层模块库，对可能用到的功能进行抽象，简化底层各设备或软件的调用方法，限制api层调用
        api层：对用户调用进行抽象，提供通用的接口
        tests层：通过api调用实现设备功能测试
    2、代码与数据分离
        conf：层次化提供数据的配置
    
项目结构
    
    1、目录结构
    .
        │
        ├─api
        │  │
        │  └─wgldnet
        │        dataframeprocess.py
        │        modeldata.py
        │
        ├─common
        │     dataunit.py
        │
        ├─conf
        │  │  libweb.py
        │  │  
        │  └─wgldnet
        │     │  compareresult.py
        │     │  compareselect.py
        │     │  outconfig.py
        │     │
        │     └─compareresultd
        │           performance.py
        │
        ├─lib                           
        │  │  __init__.py
        │  │
        │  └─web
        │        webretry.py
        │        webtable.py
        │        webunit.py
        │
        └─tests
           │
           └─codetest
               │
               └─common
                       test_dataunit.py
    
    2、结构说明:
        
        lib目录：基础底层库
        common目录：通用代码目录，独立于各模块
        api目录：用例程序接口
        conf目录：包含web元素访问配置，输出结果文件，及lib底层库的基本配置，
        
        
    
脚本使用方法
    
    1、使用环境： 
        系统：win7; 
        python 3.*
        chrome版本：69.0.3497.100; 
        chromedriver: v2.41;（chromedriver需要放置在环境变量path所在目录：如python安装目录）
        
    2、使用方法（win7）：
        a.git获取后，拷贝python运行main_get_T_M_performance.py即可（win7）
    
    3、使用方法（linux）：
        a.需要修改config/wgldnet/outconfig.py的输出配置参数“d:/result.csv”到合适的linux目录
        
    
