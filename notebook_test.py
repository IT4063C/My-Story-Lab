import my_story as result

def test_add():
  assert result.add(1, 2) == 3
  assert result.add(2, 3) == 5

def test_print(capsys):
  result.printHelloWorld()
  captured = capsys.readouterr()
  assert captured.out == 'Hello World\n'
