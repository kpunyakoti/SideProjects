# Pandemic Flu Spread in a classroom

In this project, we simulated flu spread in a classroom of 31 elementary school kids. 30 of the kids are healthy (and susceptible to flu) on Day 1. Tommy (the 31st kid) walks in with the flu and starts interacting with his potential victims. To keep things simple, let’s suppose that Tommy comes to school every day (whether or not he’s sick) and will be infectious for 3 days. Thus, there are 3 chances for Tommy to infect the other kids — Days 1, 2, and 3. Suppose that the probability that he infects any individual susceptible kid on any of the three days is p = 0.02; and suppose that all kids and days are independent (so that you have i.i.d. Bern(p) trials). If a kid gets infected by Tommy, he will then become infectious for 3 days as well, starting on the next day.

This folder contains required code to run this simulation.

## Files
- `pandemic_sim.py`:  The main simulation script.
- `requirements.txt`: File listing the required Python packages.
- `output_fils/`: Directory containing output data files and images.

## Installation
To install the required packages, use the `requirements.txt` file.

```pip install -r requirements.txt```

Alternatively you can execute the following command to install all required packages.

```pip install numpy scipy pandas matplotlib```

## Running the Simulation
To run the simulation, execute the `pandemic_sim.py` script:

```python pandemic_sim.py```

## Outputs

The script generates several output files and images in the output_files/ directory:

1. Histogram of Day 1 Infections:
- File: part_a_day1_infection_distribution.png
- Description: Distribution of the number of kids Tommy infects on Day 1.

2. Output Data (Without Immunization):
- File: output_df_without_immunization.csv
- Description: Expected number of infections over time without immunization.

3. Pandemic Duration Histogram (Without Immunization):

- File: part_d_pandemic_duration_wo_immunization.png
- Description: Histogram showing the duration of the pandemic without immunization.

4. Output Data (With Immunization):

- File: output_df_with_immunization.csv
- Description: Expected number of infections over time with a 50-50 chance of immunization.

5. Pandemic Duration Histogram (With Immunization):

- File: part_e_pandemic_duration_with_immunization.png
- Description: Histogram showing the duration of the pandemic with a 50-50 chance of immunization.

6. New Infections Trend:

- File: appendix1_new_infections_trend.png
- Description: Trend of new infections per day, comparing scenarios with and without immunization.

7. Average Daily Infections:

- File: appendix2_avg_daily_infections.png
- Description: Average number of infections per day, comparing scenarios with and without immunization.



