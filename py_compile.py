try:
    import py_compile  
    py_compile.start()  
except Exception as e:
    print(f"Error: {e}")