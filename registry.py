class ToolRegistry:

    def __init__(self):
        self.tools = {}

    # -----------------------------
    # Register a tool
    # -----------------------------

    def register(self, tool):
        self.tools[tool.name] = tool


    # -----------------------------
    # Get tool schemas
    # -----------------------------

    def get_schemas(self):

        schemas = []

        for tool in self.tools.values():

            schemas.append({
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.schema
            })

        return schemas


    # -----------------------------
    # Execute a tool
    # -----------------------------

    def execute(self, name, arguments):

        if name not in self.tools:
            return f"Error: Tool '{name}' not found."

        tool = self.tools[name]

        try:
            return tool.function(**arguments)

        except Exception as e:
            return f"Error executing '{name}': {str(e)}"