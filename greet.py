def greet(name: str = "World") -> str:
  """주어진 이름에게 인사말을 반환합니다."""
  return f"Hello, {name}!"


if __name__ == "__main__":
  print(greet())
