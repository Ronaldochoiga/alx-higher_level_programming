#include <Python.h>
#include <object.h>
#include <unicodeobject.h>
/**
 *print_python_string - prints the python string inputed
 *@p: the string holder
 *Return: void
 **/

void print_python_string(PyObject *p)
{
    const char *t = NULL;
    Py_ssize_t leng = 0;
    wchar_t *s = NULL;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        t = "compact ascii";
    else
        t = "compact unicode object";

    s = PyUnicode_AsWideCharString(p, &leng);

    printf("  t: %s\n", t);
    printf("  length: %ld\n", leng);
    printf("  value: %ls\n", s);
}
