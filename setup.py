from cx_Freeze import setup, Executable;
setup(name = "httpxls",
        version = "1.1.1",
        description = "http api",
        executables =[Executable("E:/httpaxls/httpapi.py")])