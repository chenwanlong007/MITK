/*=========================================================================

  Program:   Medical Imaging & Interaction Toolkit
  Module:    $RCSfile$
  Language:  C++
  Date:      $Date$
  Version:   $Revision$

Copyright (c) German Cancer Research Center, Division of Medical and
Biological Informatics. All rights reserved.
See MITKCopyright.txt or http://www.mitk.org/ for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notices for more information.

=========================================================================*/

#ifndef DISPLAYPOSITIONEVENT_H_HEADER_INCLUDED_C184F366
#define DISPLAYPOSITIONEVENT_H_HEADER_INCLUDED_C184F366

#include "mitkCommon.h"
#include "mitkEvent.h"
#include "mitkVector.h"


namespace mitk {

//##Documentation
//## @brief Event, which is fired after a mouse event has been invoked in a 3D-Scene.
//## 
//## @ingroup Interaction
//## 
//## Stores DisplayPosition of the Mouse.
class DisplayPositionEvent : public Event
{
  public:
    //##Documentation
    //## @brief Constructor with all necessary arguments.
    //##
    //## @params sender: the renderer that caused that event
    //##        type, button, buttonState, key: information from the Event
    //##        displPosition: the 2D Position of the mouse
    DisplayPositionEvent(BaseRenderer* sender, int type, int button, int buttonState, int key, const Point2D& displPosition);

    const Point2D& GetDisplayPosition() const;
    void SetDisplayPosition(const Point2D& displPosition) { m_DisplayPosition = displPosition; }
  private:
    Point2D m_DisplayPosition;
};

} // namespace mitk



#endif /* DISPLAYPOSITIONozsiEVENT_H_HEADER_INCLUDED_C184F366 */
