
SWARM_DESCRIPTION = {
  "includedFields": [
    {
      "fieldName": "Trans_Time",
      "fieldType": "datetime"
    },
    {
      "fieldName": "Cost",
      "fieldType": "float",
      "maxValue": 850.00,
      "minValue": 0.0
    }
  ],
  "streamDef": {
    "info": "srv_cntr_trans",
    "version": 1,
    "streams": [
      {
        "info": "Srv Cntr Trans",
        "source": "file://swiftTransPartTmp.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },

  "inferenceType": "TemporalAnomaly",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "Cost"
  },
  "iterationCount": 1,
  "swarmSize": "small"
}