class Tool:
    def __init__(self, name, description, function, schema):
        self.name = name
        self.description = description
        self.function = function
        self._schema = schema

    def schema(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self._schema
            }
        }

    def execute(self, arguments):
        return self.function(**arguments)


class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def get(self, name):
        return self.tools.get(name)

    def get_schemas(self):
        return [
            tool.schema()
            for tool in self.tools.values()
        ]

    def execute(self, name, arguments):
        tool = self.get(name)

        if tool is None:
            raise ValueError(
                f"Tool '{name}' is not registered."
            )

        return tool.execute(arguments)