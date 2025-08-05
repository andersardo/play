def entry2fields(input_string):
    #?
    return output

examples = [
    "Kävlingevägen 101. Vallkärra 5:32  10",
    "Kävlingevägen 107. Vallkärra 12:1, 28:1 och 19:1 Kyrkan  3",
    "Vallkärra 284. Vallkärra 5:18 och 5:35, Villa Walhall  83",
    "Rönnströms väg 2 och 6. Vallkärrtorn 4:5 och 4:10. Tores Hage	61"
]
result = [
    (['5:32'], '', 10),
    (['12:1', '28:1'], '19:1'], 'Kyrkan', 3),
    (['5:18', '5:35'], 'Villa Walhall', 83),
    (['4:5', '4:10'], 'Tores Hage', 61)
]
testCases = zip(examples, output)
for test in testCases:
    assert test[1] == split_string_into_components(test[0])
