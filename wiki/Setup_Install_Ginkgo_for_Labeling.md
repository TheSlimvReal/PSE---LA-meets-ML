In order to be able to use the labeling module, you need a compiled version of Ginkgo in your `$HOME`.
To create this executable, this project is shipped with a installation script for Ginkgo.

## Run the installation script

* go to the `PSE---LA-meets-ML` folder
* enter the following commands
```bash
chmod +x install_ginkgo_benchmarks.sh
./install_ginkgo_benchmarks.sh
```

If there are no errors while running the command, you can start using the labeling module.

## Debugging

To ensure everything works correctly go to the path `ginkgo/build/benchmark/reults/K80/cuda/SuiteSparse/HB/` and have a
look at the some of the files in there.

For more information contact the [Ginkgo Team](https://github.com/ginkgo-project/ginkgo).
