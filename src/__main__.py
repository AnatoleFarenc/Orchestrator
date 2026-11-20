from .ContextManager import ContextManager


def main() -> None:
    context_manager = ContextManager()
    print(context_manager.sys_prompt)
    print("\n\n########################################\n\n")
    context_manager.sys_prompt = "bibabeloula"
    print(context_manager.sys_prompt)


if __name__ == "__main__":
    main()
