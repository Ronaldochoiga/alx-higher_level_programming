#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints info abt pyth obj
 * @p: A PyObject list obj.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, a;
	const char *typ;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *variables = (PyVarObject *)p;

	size = variables->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (a = 0; a < size; a++)
	{
		typ = list->ob_item[a]->ob_type->tp_name;
		printf("Element %ld: %s\n", a, typ);
		if (strcmp(typ, "byt") == 0)
			print_python_bytes(list->ob_item[a]);
		else if (strcmp(typ, "float") == 0)
			print_python_float(list->ob_item[a]);
	}
}

/**
 * print_python_bytes - Prints info abt pyth obj
 * @p: A PyObject byte obj.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, a;
	PyBytesObject *byt = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] byt object info\n");
	if (strcmp(p->ob_type->tp_name, "byt") != 0)
	{
		printf("  [ERROR] Invalid byt Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byt->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld byt: ", size);
	for (a = 0; a < size; a++)
	{
		printf("%02hhx", byt->ob_sval[a]);
		if (a == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints info abt pyth obj
 * @p: A PyObject float obj.
 */
void print_python_float(PyObject *p)
{
	char *buf = NULL;

	PyFloatObject *flob = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buf = PyOS_double_to_string(flob->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}
