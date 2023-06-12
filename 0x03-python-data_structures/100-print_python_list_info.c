#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	long int n, i;
	PyListObject *list;

	n = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", n);
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < n; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
