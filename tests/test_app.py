import os
def checkManifest():
    assert os.path.is_file("C:\Program Files (x86)\Steam\depotcache\945361_2536144614134451205.manifest")
def checkToU():
    assert os.path.is_dir("C:\Program Files (x86)\Steam\steamapps\common\Among Us - ToU")
def checkAmongUs():
    assert os.path.is_dir("C:\Program Files (x86)\Steam\steamapps\common\Among Us")
