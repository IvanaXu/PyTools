import STPyV8

with STPyV8.JSContext() as ctxt:
    upcase = ctxt.eval("""
    ( (lowerString) => {
        return lowerString.toUpperCase();
    })
    """)
    print(upcase("hello world!"))
