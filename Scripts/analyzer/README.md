### energy_force_virial_analyzer.py

---

This script calculates and visualizes the range of properties (such as energy, forces, and virial) from the `extxyz` file.

#### Usage

The script requires at least two arguments:

- The filename of the `extxyz` file.
- The name of the property to analyze (`energy`, `force`, or `virial`).

An optional third argument (`hist`) can be provided to generate a histogram plot of the values.

```
python script.py <filename> <property> [hist]
```

#### Example

```sh
python energy_force_virial_analyzer.py dump.xyz force
```

#### Command-Line Mode Example

```
gpumdkit.sh -range dump.xyz force
```

#### Output

```
Force range: 0.03210566767721861 to 9.230115912468435
```

If you add the `[hist]` option, it will calculate the range of forces and display a histogram:

```sh
python energy_force_virial_analyzer.py dump.xyz force hist
```

<div align="center">
<img src="../../Gallery/range_force.png" width = "50%" />
</div>



### get_min_dist.py

---

This script is used to calculate the min_dist of the structures.

#### Usage

```
python get_min_dist.py <extxyz_file>
```

#### Example

```sh
python get_min_dist.py dump.xyz
```

#### Command-Line Mode Example

```
gpumdkit.sh -min_dist dump.xyz
```

#### Output

```
Minimum interatomic distance: 1.478098603206159 Å
```

NOTE: This script is fast because it does not take into account periodic boundary conditions (PBC), but in some cases it can be problematic.



### get_min_dist_pbc.py

---

This script is used to calculate the min_dist of the structures considering the PBC.

#### Usage

```
python get_min_dist_pbc.py <extxyz_file>
```

#### Example

```sh
python get_min_dist_pbc.py dump.xyz
```

#### Command-Line Mode Example

```
gpumdkit.sh -min_dist_pbc dump.xyz
```

#### Output

```
Minimum interatomic distance: 1.478098603206159 Å
```



### filter_exyz_by_value.py

---

This script filter the structures by min_dist.

#### Usage

```sh
python filter_exyz_by_value.py <extxyz_file> <min_dist>
```

#### Example

```sh
python filter_exyz_by_value.py dump.xyz 1.4
```

#### Command-Line Mode Example

```
gpumdkit.sh -filter_value dump.xyz 1.4
```

#### 

### filter_exyz_by_box.py

---

This script filter the structures by box limit.

#### Usage

```
python filter_exyz_by_box.py <extxyz_file> <min_dist>
```

#### Example

```
python filter_exyz_by_box.py dump.xyz 20
```

#### Command-Line Mode Example

```
gpumdkit.sh -filter_box dump.xyz 20
```



### filter_exyz_by_value.py

---

This script filter the structures by specified value.

#### Usage

```
python filter_exyz_by_value.py <extxyz_file> <property> <threshold>
```

- `<extxyz_file>`: The path to the input `extxyz` file.
- `<property>`: Filtering property: `energy`, `force`, or `virial`
- `<threshold>`: Threshold value for filtering

#### Example

```
python filter_exyz_by_value.py train.xyz force 20
```

#### Command-Line Mode Example

```
gpumdkit.sh -filter_value train.xyz force 20
```

This command will filter out the structure in `train.xyz` with a force greater than 20 eV/angstrom.



### time_consuming_gpumd.sh

---

This script calculates the remaining time for GPUMD.

#### Usage

```
bash time_consuming_gpumd.sh <logfile>
```

- `<logfile>`: The path to your `log` file.

#### Example

```
bash time_consuming_gpumd.sh log
```

#### Command-Line Mode Example

```
gpumdkit.sh -time gpumd <logfile>
```

#### Output

```
------------------ Time Consuming Results ------------------
num of atoms: 7168
atom*step/s : 4.85401e+06
timesteps/s : 677.178
total frames: 1050000
total time  : 0h 25min 50s
time left   : 0h 0min 0s
Progress Bar: [########################################] 100%
```



### time_consuming_nep.sh

---

This script calculates the remaining time for nep.

#### Usage

```
bash time_consuming_gpumd.sh
```

#### Example

```
bash time_consuming_nep.sh
```

#### Command-Line Mode Example

```
gpumdkit.sh -time nep
```

#### Output

```
+-----------------+-----------+-----------------+
|       Step      | Time Diff |    Time Left    |
+-----------------+-----------+-----------------+
| 300             | 1 s       | 0 h 16 m 37 s   |
| 400             | 5 s       | 1 h 23 m 0 s    |
| 500             | 5 s       | 1 h 22 m 55 s   |
```



---

Thank you for using `GPUMDkit`! If you have any questions or need further assistance, feel free to open an issue on our GitHub repository or contact Zihan YAN (yanzihan@westlake.edu.cn).
