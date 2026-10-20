from pathlib import Path
import os
import shutil
EnDek_verison = "2.7.5"
def after_update_cleanup():
    try:
        updater_path =  Path(__file__).resolve()
        Fuctionalities_folder = updater_path.parent
        EnDek_main = Fuctionalities_folder.parent
    except PermissionError:
        print("Insufficient permissions in main folder to install updates")
        return False
    except Exception as e:
        print(f"failed to index file path due to: {e}")
        return False
    try:
        shutil_zip_path = Path(os.path.join(EnDek_main.parent, "EnDek_update_file.zip"))
        shutil_backup_path = Path(os.path.join(EnDek_main.parent,".EnDek_backup_for_update"))
        shutil_zip_path.unlink(missing_ok=True)
        if Path(EnDek_main.parent/ "EnDek_update").exists():
            shutil.rmtree(Path(EnDek_main.parent/ "EnDek_update"))
        if shutil_backup_path.exists():
            shutil.rmtree(shutil_backup_path)
        return "cleaned up"
    except Exception as e:
        return f"could not clean up due to {e}."
def startup_check():
    status = False
    current_path = Path(__file__).resolve()
    functionality_path = current_path.parent
    EnDek_tree = functionality_path.parent
    EnDek_parent = EnDek_tree.parent
    if str(EnDek_tree).endswith("-main"):
        try:
            EnDek_tree.rename(EnDek_parent/ "EnDek")
            status = True 
        except Exception as e:
            print(f"""could not rename file from 'EnDek-main' to 'EnDek' due to {e}.
Please rename manually to recive further updates. """)
    elif str(EnDek_tree).endswith("-main") == False:
        status = True
    if os.path.exists(EnDek_parent/"EnDek_update"):
        after_update_cleanup()
        print(f"""You EnDek has been updated to the latest version {EnDek_verison}.
And backups have been cleared.""")
        return [status, True]
    else:
        return [status, False]