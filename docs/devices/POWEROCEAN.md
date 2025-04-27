<!-- filepath: /Users/dzhunethasan/GitHub/hassio-ecoflow-cloud/docs/devices/POWEROCEAN.md -->
## PowerOcean

*Sensors*
- Solar Power (`mpptPwr`)
- Battery SOC (`bpSoc`)
- Battery Power (`bpPwr`)
- System Load Power (`sysLoadPwr`)
- System Grid Power (`sysGridPwr`)
- String 1 Power (`mpptPv1.pwr`)
- String 1 Current (`mpptPv1.amp`)
- String 1 Voltage (`mpptPv1.vol`)
- String 2 Power (`mpptPv2.pwr`)
- String 2 Current (`mpptPv2.amp`)
- String 2 Voltage (`mpptPv2.vol`)
- Phase A Voltage (`pcsAPhase.vol`)
- Phase A Current (`pcsAPhase.amp`)
- Phase A Active Power (`pcsAPhase.actPwr`)
- Phase A Reactive Power (`pcsAPhase.reactPwr`)
- Phase A Apparent Power (`pcsAPhase.apparentPwr`)
- Phase B Voltage (`pcsBPhase.vol`)
- Phase B Current (`pcsBPhase.amp`)
- Phase B Active Power (`pcsBPhase.actPwr`)
- Phase B Reactive Power (`pcsBPhase.reactPwr`)
- Phase B Apparent Power (`pcsBPhase.apparentPwr`)
- Phase C Voltage (`pcsCPhase.vol`)
- Phase C Current (`pcsCPhase.amp`)
- Phase C Active Power (`pcsCPhase.actPwr`)
- Phase C Reactive Power (`pcsCPhase.reactPwr`)
- Phase C Apparent Power (`pcsCPhase.apparentPwr`)
- Status

*Switches*
_None_

*Sliders (numbers)*
_None_

*Selects*
_None_

## Notes
- Data structure may be nested; see code for details.
- This device is available as `PowerOcean` in the integration.

## Integration
Add your PowerOcean device via the EcoFlow Cloud integration. All sensors listed above will be available as entities.
