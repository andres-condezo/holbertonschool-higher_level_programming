#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p);

/**
 * print_python_list_info - Prints the Info of a PyObject as list
 * @p: Pointer to PyObject
*/
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *item, *list = p;
	Py_ssize_t list_len, allocated;

	list_len = PyList_Size(list);
	allocated = ((PyListObject *)list)->allocated;

	if (list_len < 0)
		return;

	printf("[*] Size of the Python List = %d\n", (int)list_len);
	printf("[*] Allocated = %d\n", (int)allocated);

	for (i = 0; i < list_len; i++)
	{
		item = PyList_GetItem(list, i);
		if (PyErr_Occurred())
			return;
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
