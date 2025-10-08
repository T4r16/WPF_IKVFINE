
import FINE as fn
import pandas as pd
import matplotlib.pyplot as plt

# Zeigen Sie alle Zeilen und Spalten des DataFrames
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Energiesysteme:
sink_1 = "sink_1_commodity"
source_1 = "source_1_commodity"
source_786 = "source_786_commodity"
source_785aSW = "source_785aSW_commodity"
source_785aNE = "source_785aNE_commodity"
source_904 = "source_904_commodity"
source_908SE = "source_908SE_commodity"
source_908NW = "source_908NW_commodity"
source_917 = "source_917_commodity"
source_FF = "source_FF_commodity"
storage_1 = "storage_1_commodity"
conversion_1 = ["source_1_commodity", "sink_1_commodity"]
conversion_2 = ["source_786_commodity", "sink_1_commodity"]
conversion_3 = ["source_785aSW_commodity", "sink_1_commodity"]
conversion_4 = ["source_785aNE_commodity", "sink_1_commodity"]
conversion_5 = ["source_904_commodity", "sink_1_commodity"]
conversion_6 = ["source_908SE_commodity", "sink_1_commodity"]
conversion_7 = ["source_908NW_commodity", "sink_1_commodity"]
conversion_8 = ["source_917_commodity", "sink_1_commodity"]
conversion_9 = ["source_FF_commodity", "sink_1_commodity"]
conversion_10 = ["storage_1_commodity", "sink_1_commodity"]
Electricity_purchase = ["Electricity_purchase_commodity"]
## Aufbau EMS

locations = {'location01'}

commodityUnitDict = {'sink_1_commodity': 'kW_el',
                     'source_1_commodity': 'kW_el',
                     'source_786_commodity': 'kW_el',
                     'source_785aSW_commodity': 'kW_el',
                     'source_785aNE_commodity': 'kW_el',
                     'source_904_commodity': 'kW_el',
                     'source_908SE_commodity': 'kW_el',
                     'source_908NW_commodity': 'kW_el',
                     'source_917_commodity': 'kW_el',
                     'source_FF_commodity': 'kW_el',
                     'storage_1_commodity': 'KW_el',
                     'Electricity_purchase_commodity': 'kW_el*h/a'
                     }

commodities = {'sink_1_commodity',
               'source_1_commodity',
               'source_786_commodity',
               'source_785aSW_commodity',
               'source_785aNE_commodity',
               'source_904_commodity',
               'source_908SE_commodity',
               'source_908NW_commodity',
               'source_917_commodity',
               'source_FF_commodity',
               'storage_1_commodity',
               'Electricity_purchase_commodity'
               }

esM = fn.EnergySystemModel(locations={"location01"},
                            commodities=commodities,
                            numberOfTimeSteps=8760,
                            commodityUnitsDict=commodityUnitDict,
                            hoursPerTimeStep=1,
                            costUnit='Euro',
                            lengthUnit='km',
                            verboseLogLevel=0)

## Sinks

# sink_1
esM.add(fn.Sink(esM=esM,
                name='sink_1',
                commodity=sink_1,
                hasCapacityVariable=False,
                operationRateFix=pd.read_excel("DataForExample/sink_1.xlsx"),
                ),
        )

## sources

# source_1
esM.add(fn.Source(esM=esM,
                  name='source_1',
                  commodity=source_1,
                  hasCapacityVariable=False,
                  commodityCost=0.1914421286

                  )
        )



# source_FF
investPerCapacity=771
esM.add(fn.Source(esM=esM,
                  name='source_FF',
                  commodity=source_FF,
                  hasCapacityVariable=True,
                  capacityMax=1275,
                  operationRateMax=pd.read_excel("DataForExample/FF.xlsx"),
                  investPerCapacity=investPerCapacity,
                  opexPerCapacity=investPerCapacity * 0.015,
                  interestRate=0.04,
                  economicLifetime=20
                  )),


# storage_1
#maxCapacity = 526
#investPerCapacity = 600
#fixCapacity = 50
#esM.add(fn.Storage(esM=esM,
                   #name='storage_1',
                  # commodity=storage_1,
                 #  hasCapacityVariable=True,
                   #capacityFix=fixCapacity,
                #   capacityMax=maxCapacity,
               #    chargeEfficiency=0.95,
              #     dischargeEfficiency=0.95,
             #      chargeRate=750 / maxCapacity,
                #   dischargeRate=750 / maxCapacity,
                   #selfDischarge=0.00003,
                  # cyclicLifetime=7000,
                 #  stateOfChargeMin=0.1,
                #   investPerCapacity=investPerCapacity,
                   #opexPerCapacity=investPerCapacity * 0.005,
                   #economicLifetime=20,
                   #interestRate=0.08))

## Conversions

# conversion_source_1
esM.add(fn.Conversion(esM=esM,
                      name='conversion_1',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_1: -1, sink_1: 1},
                      hasCapacityVariable=False))

# conversion_source_786
esM.add(fn.Conversion(esM=esM,
                      name='conversion_2',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_786: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_785aSW
esM.add(fn.Conversion(esM=esM,
                      name='conversion_3',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_785aSW: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_785aNE
esM.add(fn.Conversion(esM=esM,
                      name='conversion_4',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_785aNE: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_904 (Conversion for source_904)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_5',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_904: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_908SE (Conversion for source_908SE)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_6',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_908SE: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_908NW (Conversion for source_908NW)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_7',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_908NW: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_917 (Conversion for source_917)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_8',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_917: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_FF (Conversion for source_FF)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_9',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_FF: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_storage_1 (Conversion for storage_1)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_10',
                      physicalUnit='kW_el',
                      commodityConversionFactors={storage_1: -1, sink_1: 1},
                      hasCapacityVariable=False))


##results
esM.cluster(numberOfTypicalPeriods=7)
esM.optimize(timeSeriesAggregation=True, solver='gurobi')

# 6. Results
srcSnkSummary = esM.getOptimizationSummary("SourceSinkModel", outputLevel=1)
print(srcSnkSummary)
#storSummary = esM.getOptimizationSummary("StorageModel", outputLevel=1)
#print(storSummary)
convSummary = esM.getOptimizationSummary("ConversionModel", outputLevel=1)
print(convSummary)

# Read the data from the Excel files
sink_data = pd.read_excel("DataForExample/sink_1.xlsx")
pv_data = pd.read_excel("DataForExample/PV_786.xlsx")
pv_data = pd.read_excel("DataForExample/PV_785aSW.xlsx")
pv_data = pd.read_excel("DataForExample/PV_785aNE.xlsx")
pv_data = pd.read_excel("DataForExample/PV_904.xlsx")
pv_data = pd.read_excel("DataForExample/PV_917.xlsx")
pv_data = pd.read_excel("DataForExample/PV_908SE.xlsx")
pv_data = pd.read_excel("DataForExample/PV_908NW.xlsx")
pv_data = pd.read_excel("DataForExample/FF.xlsx")

#Get the first column name as the data column
sink_data_col = sink_data.columns[0]
pv_data_col = pv_data.columns[0]

# Create the plots
plt.figure(figsize=(16, 12))

# Plot sink data separately
plt.subplot(3, 1, 1)
plt.plot(sink_data.index, sink_data[sink_data_col], label='Sink Operation Rate', color='blue')
plt.xlabel('Time Index')
plt.ylabel('Operation Rate (kW_el)')
plt.title('Sink Operation Rate Over Time')
plt.legend()

# Plot PV data separately
plt.subplot(3, 1, 2)
plt.plot(pv_data.index, pv_data[pv_data_col], label='PV Operation Rate', color='green')
plt.xlabel('Time Index')
plt.ylabel('Operation Rate (kW_el)')
plt.title('PV Operation Rate Over Time')
plt.legend()

# Plot the two graphs overlapping
plt.subplot(3, 1, 3)
plt.plot(sink_data.index, sink_data[sink_data_col], label='Sink Operation Rate', color='blue')
plt.plot(pv_data.index, 2252* pv_data[pv_data_col], label='PV Operation Rate', color='green')
plt.xlabel('Time Index')
plt.ylabel('Operation Rate (kW_el)')
plt.title('Sink and PV Operation Rates Overlapping')
plt.legend()

plt.tight_layout()
plt.show()

fig, ax = fn.plotOperation(esM,'source_FF','location01')
fig, ax = fn.plotOperationColorMap(esM,'source_FF','location01')
ax.set_title('source_FF')
fig.savefig("source_FF.pdf", bbox_inches='tight')


fig, ax = fn.plotOperationColorMap(esM, 'source_917', 'location01')
ax.set_title('source_917')
fig.savefig("source_917.pdf", bbox_inches='tight')

plt.show()

# Stromkauf aus Netz
fig, ax = fn.plotOperationColorMap(esM, 'source_1', 'location01')
ax.set_title('source_1')
fig.savefig("source_1.pdf", bbox_inches='tight')

#gibt installierte Kapaz. PV
capacityPVOptimum = srcSnkSummary['location01'].loc[('source_FF', 'capacity', '[kW_el]')]
# # # max. Leistung, die im Jahr mit PV erzeugt werden kann
#operationRateMaxPV = data['source_FF, operationRateMax']['location01'] * capacityPVOptimum

# tatsächliche Nutzung der einzelnen Ressourcen
#usedSupplyOptimumGrid = srcSnkSummary['location01'].loc[('Electricity_purchase', 'operation', '[kW_el*h/a]')]
#usedSupplyOptimumPV = convSummary['location01'].loc[('ElectricityFrom_source_FF', 'operation', '[kW_el*h/a]')]+convSummary['location01'].loc[('ElectricityFrom source_917', 'operation', '[kW_el*h/a]')]
import FINE as fn
import pandas as pd
import matplotlib.pyplot as plt

# Zeigen Sie alle Zeilen und Spalten des DataFrames
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Energiesysteme:
sink_1 = "sink_1_commodity"
source_1 = "source_1_commodity"
source_786 = "source_786_commodity"
source_785aSW = "source_785aSW_commodity"
source_785aNE = "source_785aNE_commodity"
source_904 = "source_904_commodity"
source_908SE = "source_908SE_commodity"
source_908NW = "source_908NW_commodity"
source_917 = "source_917_commodity"
source_FF = "source_FF_commodity"
storage_1 = "storage_1_commodity"
conversion_1 = ["source_1_commodity", "sink_1_commodity"]
conversion_2 = ["source_786_commodity", "sink_1_commodity"]
conversion_3 = ["source_785aSW_commodity", "sink_1_commodity"]
conversion_4 = ["source_785aNE_commodity", "sink_1_commodity"]
conversion_5 = ["source_904_commodity", "sink_1_commodity"]
conversion_6 = ["source_908SE_commodity", "sink_1_commodity"]
conversion_7 = ["source_908NW_commodity", "sink_1_commodity"]
conversion_8 = ["source_917_commodity", "sink_1_commodity"]
conversion_9 = ["source_FF_commodity", "sink_1_commodity"]
conversion_10 = ["storage_1_commodity", "sink_1_commodity"]
Electricity_purchase = ["Electricity_purchase_commodity"]
## Aufbau EMS

locations = {'location01'}

commodityUnitDict = {'sink_1_commodity': 'kW_el',
                     'source_1_commodity': 'kW_el',
                     'source_786_commodity': 'kW_el',
                     'source_785aSW_commodity': 'kW_el',
                     'source_785aNE_commodity': 'kW_el',
                     'source_904_commodity': 'kW_el',
                     'source_908SE_commodity': 'kW_el',
                     'source_908NW_commodity': 'kW_el',
                     'source_917_commodity': 'kW_el',
                     'source_FF_commodity': 'kW_el',
                     'storage_1_commodity': 'KW_el',
                     'Electricity_purchase_commodity': 'kW_el*h/a'
                     }

commodities = {'sink_1_commodity',
               'source_1_commodity',
               'source_786_commodity',
               'source_785aSW_commodity',
               'source_785aNE_commodity',
               'source_904_commodity',
               'source_908SE_commodity',
               'source_908NW_commodity',
               'source_917_commodity',
               'source_FF_commodity',
               'storage_1_commodity',
               'Electricity_purchase_commodity'
               }

esM = fn.EnergySystemModel(locations={"location01"},
                            commodities=commodities,
                            numberOfTimeSteps=8760,
                            commodityUnitsDict=commodityUnitDict,
                            hoursPerTimeStep=1,
                            costUnit='Euro',
                            lengthUnit='km',
                            verboseLogLevel=0)

## Sinks

# sink_1
esM.add(fn.Sink(esM=esM,
                name='sink_1',
                commodity=sink_1,
                hasCapacityVariable=False,
                operationRateFix=pd.read_excel("DataForExample/sink_1.xlsx"),
                ),
        )

## sources

# source_1
esM.add(fn.Source(esM=esM,
                  name='source_1',
                  commodity=source_1,
                  hasCapacityVariable=False,
                  commodityCost=0.1914421286

                  )
        )



# source_FF
investPerCapacity=771
esM.add(fn.Source(esM=esM,
                  name='source_FF',
                  commodity=source_FF,
                  hasCapacityVariable=True,
                  capacityMax=1275,
                  operationRateMax=pd.read_excel("DataForExample/FF.xlsx"),
                  investPerCapacity=investPerCapacity,
                  opexPerCapacity=investPerCapacity * 0.015,
                  interestRate=0.04,
                  economicLifetime=20
                  )),


# storage_1
#maxCapacity = 526
#investPerCapacity = 600
#fixCapacity = 50
#esM.add(fn.Storage(esM=esM,
                   #name='storage_1',
                  # commodity=storage_1,
                 #  hasCapacityVariable=True,
                   #capacityFix=fixCapacity,
                #   capacityMax=maxCapacity,
               #    chargeEfficiency=0.95,
              #     dischargeEfficiency=0.95,
             #      chargeRate=750 / maxCapacity,
                #   dischargeRate=750 / maxCapacity,
                   #selfDischarge=0.00003,
                  # cyclicLifetime=7000,
                 #  stateOfChargeMin=0.1,
                #   investPerCapacity=investPerCapacity,
                   #opexPerCapacity=investPerCapacity * 0.005,
                   #economicLifetime=20,
                   #interestRate=0.08))

## Conversions

# conversion_source_1
esM.add(fn.Conversion(esM=esM,
                      name='conversion_1',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_1: -1, sink_1: 1},
                      hasCapacityVariable=False))

# conversion_source_786
esM.add(fn.Conversion(esM=esM,
                      name='conversion_2',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_786: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_785aSW
esM.add(fn.Conversion(esM=esM,
                      name='conversion_3',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_785aSW: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_785aNE
esM.add(fn.Conversion(esM=esM,
                      name='conversion_4',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_785aNE: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_904 (Conversion for source_904)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_5',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_904: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_908SE (Conversion for source_908SE)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_6',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_908SE: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_908NW (Conversion for source_908NW)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_7',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_908NW: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_917 (Conversion for source_917)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_8',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_917: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_source_FF (Conversion for source_FF)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_9',
                      physicalUnit='kW_el',
                      commodityConversionFactors={source_FF: -1, storage_1: 1},
                      hasCapacityVariable=False))

# conversion_storage_1 (Conversion for storage_1)
esM.add(fn.Conversion(esM=esM,
                      name='conversion_10',
                      physicalUnit='kW_el',
                      commodityConversionFactors={storage_1: -1, sink_1: 1},
                      hasCapacityVariable=False))


##results
esM.cluster(numberOfTypicalPeriods=7)
esM.optimize(timeSeriesAggregation=True, solver='gurobi')

# 6. Results
srcSnkSummary = esM.getOptimizationSummary("SourceSinkModel", outputLevel=1)
print(srcSnkSummary)
#storSummary = esM.getOptimizationSummary("StorageModel", outputLevel=1)
#print(storSummary)
convSummary = esM.getOptimizationSummary("ConversionModel", outputLevel=1)
print(convSummary)

# Read the data from the Excel files
sink_data = pd.read_excel("DataForExample/sink_1.xlsx")
pv_data = pd.read_excel("DataForExample/PV_786.xlsx")
pv_data = pd.read_excel("DataForExample/PV_785aSW.xlsx")
pv_data = pd.read_excel("DataForExample/PV_785aNE.xlsx")
pv_data = pd.read_excel("DataForExample/PV_904.xlsx")
pv_data = pd.read_excel("DataForExample/PV_917.xlsx")
pv_data = pd.read_excel("DataForExample/PV_908SE.xlsx")
pv_data = pd.read_excel("DataForExample/PV_908NW.xlsx")
pv_data = pd.read_excel("DataForExample/FF.xlsx")

#Get the first column name as the data column
sink_data_col = sink_data.columns[0]
pv_data_col = pv_data.columns[0]

# Create the plots
plt.figure(figsize=(16, 12))

# Plot sink data separately
plt.subplot(3, 1, 1)
plt.plot(sink_data.index, sink_data[sink_data_col], label='Sink Operation Rate', color='blue')
plt.xlabel('Time Index')
plt.ylabel('Operation Rate (kW_el)')
plt.title('Sink Operation Rate Over Time')
plt.legend()

# Plot PV data separately
plt.subplot(3, 1, 2)
plt.plot(pv_data.index, pv_data[pv_data_col], label='PV Operation Rate', color='green')
plt.xlabel('Time Index')
plt.ylabel('Operation Rate (kW_el)')
plt.title('PV Operation Rate Over Time')
plt.legend()

# Plot the two graphs overlapping
plt.subplot(3, 1, 3)
plt.plot(sink_data.index, sink_data[sink_data_col], label='Sink Operation Rate', color='blue')
plt.plot(pv_data.index, 2252* pv_data[pv_data_col], label='PV Operation Rate', color='green')
plt.xlabel('Time Index')
plt.ylabel('Operation Rate (kW_el)')
plt.title('Sink and PV Operation Rates Overlapping')
plt.legend()

plt.tight_layout()
plt.show()

fig, ax = fn.plotOperation(esM,'source_FF','location01')
fig, ax = fn.plotOperationColorMap(esM,'source_FF','location01')
ax.set_title('source_FF')
fig.savefig("source_FF.pdf", bbox_inches='tight')


fig, ax = fn.plotOperationColorMap(esM, 'source_917', 'location01')
ax.set_title('source_917')
fig.savefig("source_917.pdf", bbox_inches='tight')

plt.show()

# Stromkauf aus Netz
fig, ax = fn.plotOperationColorMap(esM, 'source_1', 'location01')
ax.set_title('source_1')
fig.savefig("source_1.pdf", bbox_inches='tight')

#gibt installierte Kapaz. PV
capacityPVOptimum = srcSnkSummary['location01'].loc[('source_FF', 'capacity', '[kW_el]')]
# # # max. Leistung, die im Jahr mit PV erzeugt werden kann
#operationRateMaxPV = data['source_FF, operationRateMax']['location01'] * capacityPVOptimum

# tatsächliche Nutzung der einzelnen Ressourcen
#usedSupplyOptimumGrid = srcSnkSummary['location01'].loc[('Electricity_purchase', 'operation', '[kW_el*h/a]')]
#usedSupplyOptimumPV = convSummary['location01'].loc[('ElectricityFrom_source_FF', 'operation', '[kW_el*h/a]')]+convSummary['location01'].loc[('ElectricityFrom source_917', 'operation', '[kW_el*h/a]')]