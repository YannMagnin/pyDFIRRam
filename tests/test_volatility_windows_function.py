import pytest
from pathlib import Path
from pydfirram.core.base import Generic, OperatingSystem
from pydfirram.core.renderer import Renderer
from loguru import logger
from .config import DUMP_FILE
from typing import List, Any

logger.opt(colors=True).info("<b><magenta> TEST PYDFIRRAM WINDOWS FUNCTIONS </magenta></b>")

@pytest.fixture
def generic_instance() -> Generic:
    """
        Create A generic fixture for test
    """
    os = OperatingSystem.WINDOWS
    dumpfile = Path(DUMP_FILE)
    return Generic(os, dumpfile)

def test_volatility_pslist(generic_instance: Generic) -> None:
    """
    Test the volatility PsList function
    """
    logger.opt(colors=True).info("<b><cyan>pslist</cyan></b> from volatility is running")
    output: Renderer = generic_instance.pslist()
    assert isinstance(output, Renderer), "Output is not an instance of Renderer"
    pslist_content: List[Any] = output.to_list()
    print(type(pslist_content))
    assert isinstance(pslist_content, list), "Output content is not a list"
    assert len(pslist_content) > 0, "Output list is empty"
    logger.success("TEST PASSED!")

def test_volatilty_pslist_with_args_pid(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>pslist</cyan></b> with args from volatility is running")
    output : Renderer = generic_instance.pslist(pid=[4])
    assert isinstance(output, Renderer), "Error during function execution"
    pslist_content : list = output.to_list()
    assert isinstance(pslist_content,list),"Not a list"
    assert len(pslist_content) == 1
    logger.success("TEST PASSED !")

def test_volatility_banners(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>banners</cyan></b> from volatility is running")
    output : Renderer = generic_instance.banners(pid=[4])
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_volatility_cmdline(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>cmdline</cyan></b> from volatility is running")
    output : Renderer = generic_instance.cmdline()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")
    cmdline_content : list = output.to_list()
    assert isinstance(cmdline_content,list),"Not a list"
    assert len(cmdline_content) > 0

def test_volatility_dlllist(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>dlllist</cyan></b> from volatility is running")
    output : Renderer = generic_instance.dlllist()
    assert isinstance(output, Renderer), "Error during function execution"
    dllist_content : list = output.to_list()
    assert isinstance(dllist_content,list),"Not a list"
    assert len(dllist_content) > 0
    logger.success("TEST PASSED !")

def test_bigpools(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>bigpools</cyan></b> from volatility is running")
    output : Renderer = generic_instance.bigpools()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_callbacks(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>callbacks</cyan></b> from volatility is running")
    output : Renderer = generic_instance.callbacks()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_certificates(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>certificate</cyan></b> from volatility is running")
    output : Renderer = generic_instance.certificates()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_configwriter(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>configwriter</cyan></b> from volatility is running")
    output : Renderer = generic_instance.configwriter()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_crashinfo(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>crashinfo</cyan></b> from volatility is running")
    with pytest.raises(Exception):
        generic_instance.crashinfo()
    logger.success("TEST PASSED !")

def test_devicetree(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>devicetree</cyan></b> from volatility is running")
    output : Renderer = generic_instance.devicetree()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_driverirp(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>driverirp</cyan></b> from volatility is running")
    output : Renderer = generic_instance.driverirp()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_drivermodule(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>drivermodule</cyan></b> from volatility is running")
    output : Renderer = generic_instance.drivermodule()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_driverscan(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>driverscan</cyan></b> from volatility is running")
    output : Renderer = generic_instance.driverscan()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_envars(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>envars</cyan></b> from volatility is running")
    output : Renderer = generic_instance.envars()
    assert isinstance(output, Renderer), "Error during function execution"
    envars_content : list = output.to_list()
    assert isinstance(envars_content,list),"Not a list"
    assert len(envars_content) > 0
    logger.success("TEST PASSED !")

def test_hivelist(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>hivelist</cyan></b> from volatility is running")
    output : Renderer = generic_instance.hivelist()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_hivescan(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>hivescan</cyan></b> from volatility is running")
    output : Renderer = generic_instance.hivescan()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_iat(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>iat</cyan></b> from volatility is running")
    output : Renderer = generic_instance.iat()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_info(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>info</cyan></b> from volatility is running")
    output : Renderer = generic_instance.info()
    assert isinstance(output, Renderer), "Error during function execution"
    logger.success("TEST PASSED !")

def test_pstree(generic_instance : Generic) -> None :
    logger.opt(colors=True).info("<b><cyan>pstree</cyan></b> from volatility is running")
    output : Renderer = generic_instance.pstree()
    assert isinstance(output, Renderer), "Error during function execution"
    cmdline_content : list = output.to_list()
    assert isinstance(cmdline_content,list),"Not a list"
    assert len(cmdline_content) > 0
    logger.success("TEST PASSED !")
