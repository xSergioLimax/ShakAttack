import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="tubarao.py", icon="assets/tubarão.ico"
)]


cx_Freeze.setup(
    name="SharkAttack",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]}},
    executables=arquivo
)