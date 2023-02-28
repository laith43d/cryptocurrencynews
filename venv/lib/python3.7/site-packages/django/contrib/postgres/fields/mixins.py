from django.core import checks


class CheckFieldDefaultMixin:
    _default_hint = ('<valid default>', '<invalid default>')

    def _check_default(self):
        return (
            [
                checks.Warning(
                    f"{self.__class__.__name__} default should be a callable instead of an instance so that it's not shared between all field instances.",
                    hint=(
                        'Use a callable instead, e.g., use `%s` instead of '
                        '`%s`.' % self._default_hint
                    ),
                    obj=self,
                    id='postgres.E003',
                )
            ]
            if self.has_default()
            and self.default is not None
            and not callable(self.default)
            else []
        )

    def check(self, **kwargs):
        errors = super().check(**kwargs)
        errors.extend(self._check_default())
        return errors
