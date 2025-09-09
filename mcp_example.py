"""
MCP（Model Context Protocol）Python 实例
本示例演示如何用 Python 实现一个简单的 MCP 协议模型调用与上下文管理。
"""

class ModelContext:
    """模型上下文管理类"""
    def __init__(self):
        self.context = {}

    def set(self, key, value):
        self.context[key] = value

    def get(self, key, default=None):
        return self.context.get(key, default)

    def clear(self):
        self.context.clear()

class SimpleModel:
    """简单的模型类，模拟模型推理"""
    def predict(self, input_text, context: ModelContext):
        # 使用上下文信息影响输出
        user = context.get('user', '未知用户')
        return f"用户 {user} 的输入：{input_text}，模型输出：{input_text[::-1]}"

if __name__ == "__main__":
    # 创建上下文
    ctx = ModelContext()
    ctx.set('user', '张三')

    # 创建模型
    model = SimpleModel()

    # 用户输入
    user_input = "你好，MCP！"
    # 调用模型
    output = model.predict(user_input, ctx)
    print(output)

    # 清理上下文
    ctx.clear()

"""
运行方法：
1. 将本文件保存为 mcp_example.py
2. 在命令行运行：python mcp_example.py
你将看到模型根据上下文和输入生成的输出。
"""
