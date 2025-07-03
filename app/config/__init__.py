from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["app/config/settings.yaml"],
    environments=True,
    env_switcher="ENV_FOR_DYNACONF",
)
