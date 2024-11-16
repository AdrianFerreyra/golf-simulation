# Luis Adrian Ferreyra - Mustard Challenge - Golf Simulation

This package implements a Monte Carlo Simulation of a Golf tournament based on statistics information provided un the `ratings.txt` file.

### Design
The script loads the information from the file, sequentially simulates tournaments and collects the results to calculate the simulation results and print.

The tournament simulation is handled by a min heap to order results and a map from points to players with those points. With this information we can determine ties easily.

The simulation results is handled by a manager that will add partial tournament results and then calculate averages based on the number of processed updates.

### Potential Enhancements

- Parametrising number of tournaments in module `main`.
- Parametrising the source file in module `main`.
- Adding more printers for file printing, extra information, etc.

## Example run

```
Player Name                  Win Fraction    Top 5 Fraction
-------------------------  --------------  ----------------
Sergio Garcia                   0.193881          0.468653
Tiger Woods                     0.124788          0.377062
Kenny Perry                     0.0578942         0.218078
Gonzalo Fernandez-Castano       0.0584942         0.233077
Rory McIlroy                    0.0486951         0.19898
John Cook                       0.0435956         0.189481
Jaco Van Zyl                    0.0453955         0.183782
Brandt Snedeker                 0.039796          0.216078
Francesco Molinari              0.0327967         0.19718
Matteo Manassero                0.0411959         0.142986
Rocco Mediate                   0.039896          0.135086
Phil Mickelson                  0.0350965         0.152985
Justin Rose                     0.0322968         0.147685
Jim Furyk                       0.0329967         0.151985
Luke Donald                     0.0348965         0.144086
South Africa                    0.0312969         0.208579
Charl Schwartzel                0.029897          0.194181
Duffy Waldorf                   0.0256974         0.182982
Darren Fichardt                 0.0277972         0.181082
Jay Haas                        0.0235976         0.0759924
```

## How to run

1. Install dependencies:

   ```shell
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run simulation as module:

   ```shell
   python -m src.main
   ```
