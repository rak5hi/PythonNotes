####################################################

is_connected: bool = True
has_electrisity: bool = True
has_paid: bool = True

requirements: list[bool] = [is_connected,has_electrisity,has_paid]

has_internet: bool = all(requirements)

print('Internet:', has_internet)
####################################################

sub1_fail: bool = False
sub2_fail: bool = True
sub3_fail: bool = False
 
subjects: list[bool] = [sub1_fail, sub2_fail, sub3_fail]

has_backlog: bool = any(subjects)

print('Any backlog:', has_backlog)

####################################################
