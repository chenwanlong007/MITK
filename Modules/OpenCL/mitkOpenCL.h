/*===================================================================

The Medical Imaging Interaction Toolkit (MITK)

Copyright (c) German Cancer Research Center,
Division of Medical and Biological Informatics.
All rights reserved.

This software is distributed WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.

See LICENSE.txt or http://www.mitk.org for details.

===================================================================*/

#ifndef MITKOPENCL_H_HEADER_INCLUDED
#define MITKOPENCL_H_HEADER_INCLUDED

#if defined (__APPLE__) || defined(MACOSX)
#include <OpenCL/cl.h>
#else
#define CL_USE_DEPRECATED_OPENCL_1_2_APIS
#include <CL/cl.h>
#endif

#endif /* MITKOPENCL_H_HEADER_INCLUDED */
