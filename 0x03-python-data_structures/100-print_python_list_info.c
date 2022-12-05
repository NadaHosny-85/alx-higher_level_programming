#include <stdio.h>
#include <python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function prints info
 * about a python list
 *
 * @p: pyObject
 *
 * return: void
 */

void print_python_list_info(PyObject *p)
{
	int i;

	long int size = PyList_Size(p);

	PyListObject *list = (PyListObject *)p;

	PyObject *list_elem;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		list_elem = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(list_elem)->tp_name);
	}
}
