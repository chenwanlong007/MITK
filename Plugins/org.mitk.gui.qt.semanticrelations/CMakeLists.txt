project(org_mitk_gui_qt_semanticrelations)

mitk_create_plugin(
  EXPORT_DIRECTIVE MITK_GUI_SEMANTICRELATIONS_EXPORT
  EXPORTED_INCLUDE_SUFFIXES src
  MODULE_DEPENDS MitkPersistence MitkSemanticRelationsUI MitkRenderWindowManager
)
