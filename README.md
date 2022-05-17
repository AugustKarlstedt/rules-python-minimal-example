# minimal example of bazel regression

something broke between v0.7.0 and v0.8.1 that makes it so deps are not resolved properly

to see error run

```sh
$ bazel run //:requirements.update && bazel run //:gazelle && bazel run //:build_file_generation_bin
```

to see older version working swap out the commented lines in `WORKSPACE`
