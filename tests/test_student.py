from school_schedule.student import Student

def test_Student_valid():
    adie = Student("Bella", "junior", ["History", "Science"])
    assert adie.name == "Bella"
    assert adie.grade == "junior"
    assert adie.classes == ["History", "Science"]

def test_add_class_valid():
    # arrange 
    class_name = "Math"
    # act
    adie = Student("Bella", "junior", ["History", "Science"])
    adie.add_class(class_name)
    assert adie.classes == ["History", "Science", "Math"]

def test_get_num_classes():
    adie = Student("Bella", "junior", ["History", "Science"])
    result = len(adie.classes)
    assert result == 2

def test_display_classes():
    adie = Student("Bella", "junior", ["History", "Science"])
    result = adie.display_classes()
    
    assert result == "History, Science"