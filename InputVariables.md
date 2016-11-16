# Several useful input variables of `octopus`

## Specifying type of calculation to be done

Use `CalculationMode`

- `gs`: ground state

## Specifying system dimensionality

Use `Dimensions`

## Specifying level theory

Use `TheoryLevel`


## Mesh specification

Use: `radius`, `spacing`


## Defining custom potential

An example of defining harmonic potential
```
% Species
  'X' | species_user_defined | potential_formula | "0.5*x^2" | valence | 2
%
```

TODO: what is the meaning of variable `x` ? Is is absolute position or relative
(distance from its center) ?

## Specifying 'atomic' coordinate(s)

Define 'atomic' coordinate(s) (or center(s) of potential):
```
% Coordinates
  'X' | 0
%
```

## Adding empty states

Use `ExtraStates`


## Output wavefunction:

Use:
```
Output = potential
OutputFormat = axis_x
OutputWfsNumber = "1-5"
```
