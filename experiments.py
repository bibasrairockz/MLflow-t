import mlflow

def calculator(a,b,operation=None) :
    if operation=="add":
        return (a+b)
    if operation=="sub":
        return (a-b)
    if operation=="mul":
        return (a*b)
    if operation=="div":
        return (a/b)

if __name__=="__main__":
    a, b, opt = 123,4,"mul"

    with mlflow.start_run():
        result=calculator(a,b,opt)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("opt",opt)
        print(f"my result is {result}")
        mlflow.log_param("result", result)