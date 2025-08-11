# LlamaIndex

## Env Setting

```
!pip install llama-index langchain_community "httpx==0.28.1"
```

## Code

### make Function Tools

```
import os
os.enviorn["OPEN_API_KEY"] = "{your openAPI api key}"

from llama_index.core.tools import FunctionTool
import nest_asyncio

nest_asyncio.apply()

def multiply(a: int, b: int) -> int:
  return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)

def divide(a: int, b: int) -> int:
  return a / b

divide_tool = FunctionTool.from_defaults(fn=divide)
tools = [multiply_tool, divide_tool]
```
