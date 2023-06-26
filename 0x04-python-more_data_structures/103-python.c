#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes info
 *
 * @p: Pyth objects
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, z, lim;

	printf("[.] bytes objects info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes objects\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;

	printf("  first %ld bytes:", lim);

	for (z = 0; z < lim; z++)
		if (string[z] >= 0)
			printf(" %02x", string[z]);
		else
			printf(" %02x", 256 + string[z]);

	printf("\n");
}

/**
 * print_python_list - Prints list info
 *
 * @p: Pyth objects
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, z;
	PyListObject *list;
	PyObject *ob;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (z = 0; z < size; z++)
	{
		ob = ((PyListObject *)p)->ob_item[z];
		printf("Element %ld: %s\n", z, ((ob)->ob_type)->tp_name);
		if (PyBytes_Check(ob))
			print_python_bytes(ob);
	}
}
