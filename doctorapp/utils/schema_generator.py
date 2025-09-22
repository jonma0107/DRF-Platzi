from drf_yasg.generators import OpenAPISchemaGenerator


class DoctorappSchemaGenerator(OpenAPISchemaGenerator):
  def should_include_endpoint(
    self, path: str, method: str, view, public: bool
  ) -> bool:
    return not path.endswith("{format}") and super().should_include_endpoint(
      path, method, view, public
    )
