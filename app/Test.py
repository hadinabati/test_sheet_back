a={
  "OK": True,
  "result": True,
  "data": [
    {
      "name": "دبیرستان راه رشد",
      "address": "شهرک غرب نرسیده به یه جایی",
      "kind": True,
      "token": "5e5e40344fc2b022",
      "paye": "دوره ی دوم ",
      "classes": [
        {
          "name": "دهم",
          "token": "f6108402841117c9"
        }
      ]
    }
  ]
}
b=a['data'][0]
print(b['classes'])