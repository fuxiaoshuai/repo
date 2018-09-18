多包情况下使用模块

    第一种：在同目录的文档中创建模块，可直接导入 impotr modules
	
    第二种：在目录中创建模块文件夹，在文件夹中创建__init__.py空文件即可创建模块包

不同包之间模块导入及使用方法
导入包的几种方法：
        import modules(文件夹).modules(文件)
        import modules(文件夹).modules(文件) as f(别名)
        from modules(文件夹) import modules(文件)
        from modules.modules(文件夹+文件名) import xxx(类或方法)
